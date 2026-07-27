"""Billing engine — converts usage records into invoices.

Uses configurable pricing tiers and supports per-org billing cycles.
This avoids the Proxmox problem of having no billing built in and the
OpenStack problem of needing separate systems like CloudKitty.
"""

import logging
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from enum import Enum
from typing import Any, Dict, List, Optional

from billing.meter import ResourceUsage, UsageMeter

logger = logging.getLogger(__name__)


class InvoiceStatus(str, Enum):
    DRAFT = "draft"
    PENDING = "pending"
    PAID = "paid"
    OVERDUE = "overdue"
    CANCELLED = "cancelled"


@dataclass
class InvoiceLineItem:
    """A single line on an invoice."""
    description: str
    quantity: float
    unit: str
    unit_price: float
    total: float
    metric: str = ""


@dataclass
class Invoice:
    """A periodic bill for an organization."""
    id: str
    org_id: str
    org_name: str
    period_start: datetime
    period_end: datetime
    line_items: List[InvoiceLineItem] = field(default_factory=list)
    subtotal: float = 0.0
    discount: float = 0.0
    tax_rate: float = 0.0
    tax_amount: float = 0.0
    total: float = 0.0
    currency: str = "USD"
    status: InvoiceStatus = InvoiceStatus.DRAFT
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    paid_at: Optional[datetime] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def calculate(self) -> None:
        """Compute subtotal, tax, and total."""
        self.subtotal = sum(item.total for item in self.line_items)
        self.tax_amount = round(self.subtotal * self.tax_rate, 2)
        self.total = round(self.subtotal - self.discount + self.tax_amount, 2)


# Default pricing (matching existing config.py PRICING)
DEFAULT_PRICING: Dict[str, float] = {
    "cpu_per_core_hour": 0.0068,
    "memory_per_gb_hour": 0.0034,
    "storage_per_gb_hour": 0.00014,
    "network_per_gb": 0.05,
    "snapshot_per_gb_month": 0.05,
    "backup_per_gb_month": 0.03,
}


class BillingEngine:
    """Generates invoices from usage data."""

    def __init__(self, pricing: Optional[Dict[str, float]] = None):
        self.pricing = pricing or dict(DEFAULT_PRICING)
        self._invoices: Dict[str, Invoice] = {}

    def set_pricing(self, key: str, value: float) -> None:
        """Override a pricing parameter."""
        self.pricing[key] = value

    async def generate_invoice(
        self,
        org_id: str,
        org_name: str,
        usage_records: List[ResourceUsage],
        period_start: datetime,
        period_end: datetime,
        invoice_id: str = "",
    ) -> Invoice:
        """Create an invoice from a set of usage records."""
        from uuid import uuid4

        line_items: List[InvoiceLineItem] = []
        hours = max((period_end - period_start).total_seconds() / 3600, 1)
        instance_hours: Dict[str, float] = {}

        for rec in usage_records:
            key = rec.instance_id
            instance_hours[key] = instance_hours.get(key, 0) + hours

        # CPU
        total_cpu_hours = sum(
            rec.cpu_cores * instance_hours.get(rec.instance_id, hours)
            for rec in usage_records
        )
        cpu_cost = total_cpu_hours * self.pricing["cpu_per_core_hour"]
        line_items.append(
            InvoiceLineItem(
                description="vCPU usage",
                quantity=round(total_cpu_hours, 2),
                unit="core-hours",
                unit_price=self.pricing["cpu_per_core_hour"],
                total=round(cpu_cost, 2),
                metric="cpu_cores",
            )
        )

        # Memory
        total_memory_gb_hours = sum(
            (rec.memory_mb / 1024) * instance_hours.get(rec.instance_id, hours)
            for rec in usage_records
        )
        mem_cost = total_memory_gb_hours * self.pricing["memory_per_gb_hour"]
        line_items.append(
            InvoiceLineItem(
                description="RAM usage",
                quantity=round(total_memory_gb_hours, 2),
                unit="GB-hours",
                unit_price=self.pricing["memory_per_gb_hour"],
                total=round(mem_cost, 2),
                metric="memory_mb",
            )
        )

        # Storage
        total_storage_gb_hours = sum(
            rec.storage_gb * instance_hours.get(rec.instance_id, hours)
            for rec in usage_records
        )
        storage_cost = total_storage_gb_hours * self.pricing["storage_per_gb_hour"]
        line_items.append(
            InvoiceLineItem(
                description="Block storage",
                quantity=round(total_storage_gb_hours, 2),
                unit="GB-hours",
                unit_price=self.pricing["storage_per_gb_hour"],
                total=round(storage_cost, 2),
                metric="storage_gb",
            )
        )

        # Network
        total_rx_gb = sum(rec.network_rx_bytes for rec in usage_records) / (1024**3)
        total_tx_gb = sum(rec.network_tx_bytes for rec in usage_records) / (1024**3)
        total_network_gb = total_rx_gb + total_tx_gb
        network_cost = total_network_gb * self.pricing["network_per_gb"]
        if network_cost > 0:
            line_items.append(
                InvoiceLineItem(
                    description="Data transfer",
                    quantity=round(total_network_gb, 4),
                    unit="GB",
                    unit_price=self.pricing["network_per_gb"],
                    total=round(network_cost, 2),
                    metric="network",
                )
            )

        invoice = Invoice(
            id=invoice_id or str(uuid4()),
            org_id=org_id,
            org_name=org_name,
            period_start=period_start,
            period_end=period_end,
            line_items=line_items,
        )
        invoice.calculate()
        self._invoices[invoice.id] = invoice
        return invoice

    def get_invoice(self, invoice_id: str) -> Optional[Invoice]:
        return self._invoices.get(invoice_id)

    def list_invoices(self, org_id: str) -> List[Invoice]:
        return [inv for inv in self._invoices.values() if inv.org_id == org_id]

    def mark_paid(self, invoice_id: str) -> bool:
        invoice = self._invoices.get(invoice_id)
        if not invoice:
            return False
        invoice.status = InvoiceStatus.PAID
        invoice.paid_at = datetime.now(timezone.utc)
        return True

    def mark_overdue(self, invoice_id: str) -> bool:
        invoice = self._invoices.get(invoice_id)
        if not invoice:
            return False
        invoice.status = InvoiceStatus.OVERDUE
        return True
