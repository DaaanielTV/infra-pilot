"""Tests for the usage metering and billing engine."""

from datetime import datetime, timedelta, timezone
from unittest.mock import AsyncMock, patch

import pytest

from billing.billing_engine import BillingEngine, Invoice, InvoiceLineItem, InvoiceStatus
from billing.meter import ResourceUsage, UsageMeter


class TestUsageMeter:
    @pytest.mark.asyncio
    async def test_collect_returns_list(self):
        meter = UsageMeter()
        results = await meter.collect()
        assert isinstance(results, list)

    def test_get_usage_for_org(self):
        meter = UsageMeter()
        now = datetime.now(timezone.utc)
        rec = ResourceUsage(
            instance_id="i-1",
            instance_name="test",
            org_id="org-1",
            project_id="proj-1",
            provider="docker",
            cpu_cores=2,
            memory_mb=1024,
            storage_gb=50,
            collected_at=now,
        )
        meter._buffer.append(rec)
        result = meter.get_usage_for_org("org-1")
        assert len(result) == 1
        assert result[0].instance_id == "i-1"

        filtered = meter.get_usage_for_org("org-2")
        assert len(filtered) == 0

    def test_clear_buffer(self):
        meter = UsageMeter()
        meter._buffer.append(
            ResourceUsage(
                instance_id="i-1", instance_name="t", org_id="o", project_id="p",
                provider="d", cpu_cores=1, memory_mb=512, storage_gb=10,
            )
        )
        assert meter.clear_buffer() == 1
        assert len(meter._buffer) == 0


class TestBillingEngine:
    def setup_method(self):
        self.engine = BillingEngine()
        self.now = datetime.now(timezone.utc)
        self.last_month = self.now - timedelta(days=30)

    def _make_usage(self, cpu=2, memory=2048, storage=50, network_rx=10**9, network_tx=10**9):
        return ResourceUsage(
            instance_id="i-1",
            instance_name="web-01",
            org_id="org-1",
            project_id="proj-1",
            provider="docker",
            cpu_cores=cpu,
            memory_mb=memory,
            storage_gb=storage,
            network_rx_bytes=network_rx,
            network_tx_bytes=network_tx,
            collected_at=self.now,
        )

    @pytest.mark.asyncio
    async def test_generate_invoice_basic(self):
        usage = [self._make_usage()]
        invoice = await self.engine.generate_invoice(
            "org-1", "Test Org", usage, self.last_month, self.now
        )
        assert invoice.org_id == "org-1"
        assert invoice.org_name == "Test Org"
        assert len(invoice.line_items) >= 3  # CPU, memory, storage, maybe network
        assert invoice.total > 0
        assert invoice.status == InvoiceStatus.DRAFT

    @pytest.mark.asyncio
    async def test_invoice_calculation(self):
        usage = [self._make_usage(cpu=4, memory=8192, storage=200)]
        invoice = await self.engine.generate_invoice(
            "org-1", "Test Org", usage, self.last_month, self.now
        )
        cpu_item = next(i for i in invoice.line_items if i.metric == "cpu_cores")
        assert cpu_item.unit_price == self.engine.pricing["cpu_per_core_hour"]
        assert cpu_item.total > 0
        assert invoice.subtotal == sum(i.total for i in invoice.line_items)
        assert invoice.total >= invoice.subtotal

    @pytest.mark.asyncio
    async def test_multiple_instances(self):
        recs = [
            ResourceUsage(
                instance_id="i-a", instance_name="web-a", org_id="org-1",
                project_id="proj-1", provider="docker",
                cpu_cores=1, memory_mb=512, storage_gb=10,
                collected_at=self.now,
            ),
            ResourceUsage(
                instance_id="i-b", instance_name="web-b", org_id="org-1",
                project_id="proj-1", provider="docker",
                cpu_cores=2, memory_mb=1024, storage_gb=20,
                collected_at=self.now,
            ),
        ]
        invoice = await self.engine.generate_invoice(
            "org-1", "Test Org", recs, self.last_month, self.now
        )
        assert invoice.subtotal > 0

    def test_mark_paid(self):
        inv = Invoice(id="inv-1", org_id="org-1", org_name="T",
                       period_start=self.last_month, period_end=self.now)
        self.engine._invoices["inv-1"] = inv
        assert self.engine.mark_paid("inv-1") is True
        assert inv.status == InvoiceStatus.PAID
        assert inv.paid_at is not None

    def test_mark_overdue(self):
        inv = Invoice(id="inv-2", org_id="org-1", org_name="T",
                       period_start=self.last_month, period_end=self.now)
        self.engine._invoices["inv-2"] = inv
        assert self.engine.mark_overdue("inv-2") is True
        assert inv.status == InvoiceStatus.OVERDUE

    def test_list_invoices(self):
        for i in range(3):
            self.engine._invoices[f"inv-{i}"] = Invoice(
                id=f"inv-{i}", org_id="org-1", org_name="T",
                period_start=self.last_month, period_end=self.now,
            )
        assert len(self.engine.list_invoices("org-1")) == 3

    def test_set_pricing(self):
        self.engine.set_pricing("cpu_per_core_hour", 0.01)
        assert self.engine.pricing["cpu_per_core_hour"] == 0.01

    def test_custom_pricing(self):
        engine = BillingEngine(pricing={"cpu_per_core_hour": 0.005})
        assert engine.pricing["cpu_per_core_hour"] == 0.005
