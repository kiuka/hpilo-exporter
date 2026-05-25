from prometheus_client import CollectorRegistry, Gauge

LABELS = ["product_name", "server_name"]

# (key used by exporter, metric name, help text)
GAUGE_SPECS = [
    ('hpilo_vrm_gauge', 'hpilo_vrm', 'HP iLO vrm status'),
    ('hpilo_drive_gauge', 'hpilo_drive', 'HP iLO drive status'),
    ('hpilo_battery_gauge', 'hpilo_battery', 'HP iLO battery status'),
    ('hpilo_storage_gauge', 'hpilo_storage', 'HP iLO storage status'),
    ('hpilo_fans_gauge', 'hpilo_fans', 'HP iLO fans status'),
    ('hpilo_bios_hardware_gauge', 'hpilo_bios_hardware', 'HP iLO bios_hardware status'),
    ('hpilo_memory_gauge', 'hpilo_memory', 'HP iLO memory status'),
    ('hpilo_power_supplies_gauge', 'hpilo_power_supplies', 'HP iLO power_supplies status'),
    ('hpilo_processor_gauge', 'hpilo_processor', 'HP iLO processor status'),
    ('hpilo_network_gauge', 'hpilo_network', 'HP iLO network status'),
    ('hpilo_temperature_gauge', 'hpilo_temperature', 'HP iLO temperature status'),
    ('hpilo_firmware_version', 'hpilo_firmware_version', 'HP iLO firmware version'),
    ('hpilo_present_power_reading', 'hpilo_present_power_reading', 'HP iLO present power reading'),
]


def build_metrics():
    # Fresh registry per scrape so transient fallbacks (e.g. product_name =
    # "Unknown HP Server") don't leave stale labelsets in a shared registry.
    registry = CollectorRegistry()
    gauges = {
        key: Gauge(name, description, LABELS, registry=registry)
        for key, name, description in GAUGE_SPECS
    }
    return registry, gauges
