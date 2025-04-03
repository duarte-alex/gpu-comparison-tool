from .models import GCPZone, GCPZoneNames

ZONES = [
    GCPZone(name=GCPZoneNames.US_CENTRAL1_A, carbon_intensity=430),
    GCPZone(name=GCPZoneNames.US_EAST1_B, carbon_intensity=560),
    # Add more zones as needed
]

ZONES_BY_NAME = {zone.name: zone for zone in ZONES}