"""Tests for the region and federation modules."""

import pytest
from region.federation import Federation, FederationPeer, PeerStatus
from region.region import Datacenter, Region, RegionStatus


class TestDatacenter:
    def test_default_values(self):
        dc = Datacenter(id="dc-1", name="us-east-1a", region_id="us-east")
        assert dc.status == RegionStatus.ACTIVE
        assert dc.cpu_available == 0
        assert dc.memory_available == 0

    def test_utilization(self):
        dc = Datacenter(
            id="dc-1",
            name="test",
            region_id="r1",
            total_cpu_cores=100,
            used_cpu_cores=30,
            total_memory_mb=102400,
            used_memory_mb=51200,
            total_storage_gb=10000,
            used_storage_gb=2000,
        )
        util = dc.utilization()
        assert util["cpu_percent"] == 30.0
        assert util["memory_percent"] == 50.0
        assert util["storage_percent"] == 20.0

    def test_available_resources(self):
        dc = Datacenter(
            id="dc-1",
            name="test",
            region_id="r1",
            total_cpu_cores=64,
            used_cpu_cores=16,
            total_memory_mb=524288,
            used_memory_mb=131072,
            total_storage_gb=50000,
            used_storage_gb=10000,
        )
        assert dc.cpu_available == 48
        assert dc.memory_available == 393216
        assert dc.storage_available == 40000


class TestRegion:
    def test_create_region(self):
        r = Region(id="us-east", name="US East", display_name="US East (Virginia)")
        assert r.status == RegionStatus.ACTIVE
        assert len(r.datacenters) == 0

    def test_add_and_get_datacenter(self):
        r = Region(id="us-east", name="US East")
        dc = Datacenter(id="dc-1", name="us-east-1a", region_id="us-east")
        r.add_datacenter(dc)
        assert len(r.datacenters) == 1
        assert r.get_datacenter("dc-1") is dc

    def test_remove_datacenter(self):
        r = Region(id="us-east", name="US East")
        r.add_datacenter(Datacenter(id="dc-1", name="a", region_id="us-east"))
        r.add_datacenter(Datacenter(id="dc-2", name="b", region_id="us-east"))
        assert r.remove_datacenter("dc-1") is True
        assert len(r.datacenters) == 1
        assert r.remove_datacenter("nonexistent") is False

    def test_totals(self):
        r = Region(id="us-east", name="US East")
        r.add_datacenter(
            Datacenter(
                id="dc-1",
                name="a",
                region_id="us-east",
                total_cpu_cores=32,
                total_memory_mb=262144,
                total_storage_gb=20000,
            )
        )
        r.add_datacenter(
            Datacenter(
                id="dc-2",
                name="b",
                region_id="us-east",
                total_cpu_cores=32,
                total_memory_mb=262144,
                total_storage_gb=20000,
            )
        )
        assert r.total_cpu == 64
        assert r.total_memory == 524288
        assert r.total_storage == 40000

    def test_to_dict(self):
        r = Region(id="eu-west", name="EU West", display_name="EU West (Ireland)")
        r.add_datacenter(Datacenter(id="dc-1", name="eu-west-1a", region_id="eu-west"))
        d = r.to_dict()
        assert d["id"] == "eu-west"
        assert d["name"] == "EU West"
        assert len(d["datacenters"]) == 1


class TestFederation:
    def test_register_peer(self):
        f = Federation()
        peer = FederationPeer(
            id="p1", name="remote-us", api_url="https://us.infra-pilot.local"
        )
        f.register_peer(peer)
        assert f.get_peer("p1") is peer

    def test_unregister_peer(self):
        f = Federation()
        f.register_peer(
            FederationPeer(id="p1", name="test", api_url="http://localhost")
        )
        assert f.unregister_peer("p1") is True
        assert f.get_peer("p1") is None

    def test_list_peers(self):
        f = Federation()
        f.register_peer(FederationPeer(id="p1", name="a", api_url="http://a.local"))
        f.register_peer(FederationPeer(id="p2", name="b", api_url="http://b.local"))
        assert len(f.list_peers()) == 2

    def test_peer_defaults(self):
        peer = FederationPeer(id="p1", name="test", api_url="http://localhost")
        assert peer.status == PeerStatus.UNKNOWN
        assert peer.timeout_seconds == 10
