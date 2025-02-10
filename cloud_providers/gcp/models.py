from enum import Enum
from pydantic import BaseModel
from typing import Optional

## ================================
## Classes
## ================================


class GCPZoneNames(str, Enum):
    """All zones in Google Cloud Platform"""

    US_CENTRAL1 = "us-central1"
    US_CENTRAL1_B = "us-central1-b"
    US_CENTRAL1_C = "us-central1-c"
    US_CENTRAL1_F = "us-central1-f"
    US_EAST1_B = "us-east1-b"
    US_EAST1_C = "us-east1-c"
    US_EAST1_D = "us-east1-d"
    US_EAST4_A = "us-east4-a"
    US_EAST4_B = "us-east4-b"
    US_EAST4_C = "us-east4-c"
    US_EAST5_A = "us-east5-a"
    US_EAST5_B = "us-east5-b"
    US_EAST5_C = "us-east5-c"
    US_WEST1_A = "us-west1-a"
    US_WEST1_B = "us-west1-b"
    US_WEST1_C = "us-west1-c"
    US_WEST2_A = "us-west2-a"
    US_WEST2_B = "us-west2-b"
    US_WEST2_C = "us-west2-c"
    US_WEST3_A = "us-west3-a"
    US_WEST3_B = "us-west3-b"
    US_WEST3_C = "us-west3-c"
    US_WEST4_A = "us-west4-a"
    US_WEST4_B = "us-west4-b"
    US_WEST4_C = "us-west4-c"
    NORTHAMERICA_NORTHEAST1_A = "northamerica-northeast1-a"
    NORTHAMERICA_NORTHEAST1_B = "northamerica-northeast1-b"
    NORTHAMERICA_NORTHEAST1_C = "northamerica-northeast1-c"
    NORTHAMERICA_NORTHEAST2_A = "northamerica-northeast2-a"
    NORTHAMERICA_NORTHEAST2_B = "northamerica-northeast2-b"
    NORTHAMERICA_NORTHEAST2_C = "northamerica-northeast2-c"
    NORTHAMERICA_SOUTH1_A = "northamerica-south1-a"
    NORTHAMERICA_SOUTH1_B = "northamerica-south1-b"
    NORTHAMERICA_SOUTH1_C = "northamerica-south1-c"
    US_SOUTH1_A = "us-south1-a"
    US_SOUTH1_B = "us-south1-b"
    US_SOUTH1_C = "us-south1-c"
    EUROPE_NORTH1_A = "europe-north1-a"
    EUROPE_NORTH1_B = "europe-north1-b"
    EUROPE_NORTH1_C = "europe-north1-c"
    EUROPE_CENTRAL2_A = "europe-central2-a"
    EUROPE_CENTRAL2_B = "europe-central2-b"
    EUROPE_CENTRAL2_C = "europe-central2-c"
    EUROPE_SOUTHWEST1_A = "europe-southwest1-a"
    EUROPE_SOUTHWEST1_B = "europe-southwest1-b"
    EUROPE_SOUTHWEST1_C = "europe-southwest1-c"
    EUROPE_WEST1_B = "europe-west1-b"
    EUROPE_WEST1_C = "europe-west1-c"
    EUROPE_WEST1_D = "europe-west1-d"
    EUROPE_WEST2_A = "europe-west2-a"
    EUROPE_WEST2_B = "europe-west2-b"
    EUROPE_WEST2_C = "europe-west2-c"
    EUROPE_WEST3_A = "europe-west3-a"
    EUROPE_WEST3_B = "europe-west3-b"
    EUROPE_WEST3_C = "europe-west3-c"
    EUROPE_WEST4_A = "europe-west4-a"
    EUROPE_WEST4_B = "europe-west4-b"
    EUROPE_WEST4_C = "europe-west4-c"
    EUROPE_WEST6_A = "europe-west6-a"
    EUROPE_WEST6_B = "europe-west6-b"
    EUROPE_WEST6_C = "europe-west6-c"
    EUROPE_WEST8_A = "europe-west8-a"
    EUROPE_WEST8_B = "europe-west8-b"
    EUROPE_WEST8_C = "europe-west8-c"
    EUROPE_WEST9_A = "europe-west9-a"
    EUROPE_WEST9_B = "europe-west9-b"
    EUROPE_WEST9_C = "europe-west9-c"
    EUROPE_WEST10_A = "europe-west10-a"
    EUROPE_WEST10_B = "europe-west10-b"
    EUROPE_WEST10_C = "europe-west10-c"
    EUROPE_WEST12_A = "europe-west12-a"
    EUROPE_WEST12_B = "europe-west12-b"
    EUROPE_WEST12_C = "europe-west12-c"
    ASIA_EAST1_A = "asia-east1-a"
    ASIA_EAST1_B = "asia-east1-b"
    ASIA_EAST1_C = "asia-east1-c"
    ASIA_EAST2_A = "asia-east2-a"
    ASIA_EAST2_B = "asia-east2-b"
    ASIA_EAST2_C = "asia-east2-c"
    ASIA_NORTHEAST1_A = "asia-northeast1-a"
    ASIA_NORTHEAST1_B = "asia-northeast1-b"
    ASIA_NORTHEAST1_C = "asia-northeast1-c"
    ASIA_NORTHEAST2_A = "asia-northeast2-a"
    ASIA_NORTHEAST2_B = "asia-northeast2-b"
    ASIA_NORTHEAST2_C = "asia-northeast2-c"
    ASIA_NORTHEAST3_A = "asia-northeast3-a"
    ASIA_NORTHEAST3_B = "asia-northeast3-b"
    ASIA_NORTHEAST3_C = "asia-northeast3-c"
    ASIA_SOUTH1_A = "asia-south1-a"
    ASIA_SOUTH1_B = "asia-south1-b"
    ASIA_SOUTH1_C = "asia-south1-c"
    ASIA_SOUTH2_A = "asia-south2-a"
    ASIA_SOUTH2_B = "asia-south2-b"
    ASIA_SOUTH2_C = "asia-south2-c"
    ASIA_SOUTHEAST1_A = "asia-southeast1-a"
    ASIA_SOUTHEAST1_B = "asia-southeast1-b"
    ASIA_SOUTHEAST1_C = "asia-southeast1-c"
    ASIA_SOUTHEAST2_A = "asia-southeast2-a"
    ASIA_SOUTHEAST2_B = "asia-southeast2-b"
    ASIA_SOUTHEAST2_C = "asia-southeast2-c"
    AUSTRALIA_SOUTHEAST1_A = "australia-southeast1-a"
    AUSTRALIA_SOUTHEAST1_B = "australia-southeast1-b"
    AUSTRALIA_SOUTHEAST1_C = "australia-southeast1-c"
    AUSTRALIA_SOUTHEAST2_A = "australia-southeast2-a"
    AUSTRALIA_SOUTHEAST2_B = "australia-southeast2-b"
    AUSTRALIA_SOUTHEAST2_C = "australia-southeast2-c"
    SOUTHAMERICA_EAST1_A = "southamerica-east1-a"
    SOUTHAMERICA_EAST1_B = "southamerica-east1-b"
    SOUTHAMERICA_EAST1_C = "southamerica-east1-c"
    SOUTHAMERICA_WEST1_A = "southamerica-west1-a"
    SOUTHAMERICA_WEST1_B = "southamerica-west1-b"
    SOUTHAMERICA_WEST1_C = "southamerica-west1-c"
    AFRICA_SOUTH1_A = "africa-south1-a"
    AFRICA_SOUTH1_B = "africa-south1-b"
    AFRICA_SOUTH1_C = "africa-south1-c"
    ME_CENTRAL1_A = "me-central1-a"
    ME_CENTRAL1_B = "me-central1-b"
    ME_CENTRAL1_C = "me-central1-c"
    ME_CENTRAL2_A = "me-central2-a"
    ME_CENTRAL2_B = "me-central2-b"
    ME_CENTRAL2_C = "me-central2-c"
    ME_WEST1_A = "me-west1-a"
    ME_WEST1_B = "me-west1-b"
    ME_WEST1_C = "me-west1-c"


class GCPGPUNames(str, Enum):
    NVIDIA_TESLA_P100 = "NVIDIA TESLA P100"
    NVIDIA_V100 = "NVIDIA V100"
    NVIDIA_A100_40GB = "NVIDIA A100 40GB"
    NVIDIA_A100_80GB = "NVIDIA A100 80GB"
    NVIDIA_H100_80GB = "NVIDIA H100 80GB"
    NVIDIA_H100_80GB_MEGA = "NVIDIA H100 80GB MEGA"
    NVIDIA_T4 = "NVIDIA T4"
    NVIDIA_L4 = "NVIDIA L4"
    NVIDIA_TESLA_P4 = "NVIDIA TESLA P4"
    NVIDIA_H200_141GB = "NVIDIA H200 141GB"


class GCPGPU(BaseModel):
    """Model for GCP GPU with efficiency data"""

    name: GCPGPUNames
    efficiency: float


class GCPZone(BaseModel):
    name: GCPZoneNames
    carbon_intensity: int


# API Return Types


class GCPAcceleratorAPIType(BaseModel):
    """Model for GCP Accelerator (GPU) type"""

    # id: str
    # creationTimestamp: str
    # name: str
    description: str
    zone: str
    # selfLink: str
    maximumCardsPerInstance: int
    kind: Optional[str] = None


class GPU(BaseModel):
    """Model for GCP GPU"""

    name: GCPGPUNames
    zone: GCPZoneNames
    maximumCardsPerInstance: int


class GCPAcceleratorTypeList(BaseModel):
    """Model for GCP Accelerator Types List Response"""

    id: str
    # kind: Optional[str] = None
    items: Optional[list[GCPAcceleratorAPIType]] = []


## ================================
## Constants
## ================================

ZONES: list[GCPZone] = [
    # US Central
    GCPZone(name=GCPZoneNames.US_CENTRAL1_A, carbon_intensity=430),
    GCPZone(name=GCPZoneNames.US_CENTRAL1_B, carbon_intensity=430),
    GCPZone(name=GCPZoneNames.US_CENTRAL1_C, carbon_intensity=430),
    GCPZone(name=GCPZoneNames.US_CENTRAL1_F, carbon_intensity=430),
    # US East
    GCPZone(name=GCPZoneNames.US_EAST1_B, carbon_intensity=560),
    GCPZone(name=GCPZoneNames.US_EAST1_C, carbon_intensity=560),
    GCPZone(name=GCPZoneNames.US_EAST1_D, carbon_intensity=560),
    GCPZone(name=GCPZoneNames.US_EAST4_A, carbon_intensity=322),
    GCPZone(name=GCPZoneNames.US_EAST4_B, carbon_intensity=322),
    GCPZone(name=GCPZoneNames.US_EAST4_C, carbon_intensity=322),
    GCPZone(name=GCPZoneNames.US_EAST5_A, carbon_intensity=322),
    GCPZone(name=GCPZoneNames.US_EAST5_B, carbon_intensity=322),
    GCPZone(name=GCPZoneNames.US_EAST5_C, carbon_intensity=322),
    # US West
    GCPZone(name=GCPZoneNames.US_WEST1_A, carbon_intensity=94),
    GCPZone(name=GCPZoneNames.US_WEST1_B, carbon_intensity=94),
    GCPZone(name=GCPZoneNames.US_WEST1_C, carbon_intensity=94),
    GCPZone(name=GCPZoneNames.US_WEST2_A, carbon_intensity=198),
    GCPZone(name=GCPZoneNames.US_WEST2_B, carbon_intensity=198),
    GCPZone(name=GCPZoneNames.US_WEST2_C, carbon_intensity=198),
    GCPZone(name=GCPZoneNames.US_WEST3_A, carbon_intensity=588),
    GCPZone(name=GCPZoneNames.US_WEST3_B, carbon_intensity=588),
    GCPZone(name=GCPZoneNames.US_WEST3_C, carbon_intensity=588),
    GCPZone(name=GCPZoneNames.US_WEST4_A, carbon_intensity=373),
    GCPZone(name=GCPZoneNames.US_WEST4_B, carbon_intensity=373),
    GCPZone(name=GCPZoneNames.US_WEST4_C, carbon_intensity=373),
    # US South
    GCPZone(name=GCPZoneNames.US_SOUTH1_A, carbon_intensity=321),
    GCPZone(name=GCPZoneNames.US_SOUTH1_B, carbon_intensity=321),
    GCPZone(name=GCPZoneNames.US_SOUTH1_C, carbon_intensity=321),
    # North America
    GCPZone(name=GCPZoneNames.NORTHAMERICA_NORTHEAST1_A, carbon_intensity=2),
    GCPZone(name=GCPZoneNames.NORTHAMERICA_NORTHEAST1_B, carbon_intensity=2),
    GCPZone(name=GCPZoneNames.NORTHAMERICA_NORTHEAST1_C, carbon_intensity=2),
    GCPZone(name=GCPZoneNames.NORTHAMERICA_NORTHEAST2_A, carbon_intensity=47),
    GCPZone(name=GCPZoneNames.NORTHAMERICA_NORTHEAST2_B, carbon_intensity=47),
    GCPZone(name=GCPZoneNames.NORTHAMERICA_NORTHEAST2_C, carbon_intensity=47),
    # Europe
    GCPZone(name=GCPZoneNames.EUROPE_NORTH1_A, carbon_intensity=46),
    GCPZone(name=GCPZoneNames.EUROPE_NORTH1_B, carbon_intensity=46),
    GCPZone(name=GCPZoneNames.EUROPE_NORTH1_C, carbon_intensity=46),
    GCPZone(name=GCPZoneNames.EUROPE_CENTRAL2_A, carbon_intensity=723),
    GCPZone(name=GCPZoneNames.EUROPE_CENTRAL2_B, carbon_intensity=723),
    GCPZone(name=GCPZoneNames.EUROPE_CENTRAL2_C, carbon_intensity=723),
    GCPZone(name=GCPZoneNames.EUROPE_WEST1_B, carbon_intensity=122),
    GCPZone(name=GCPZoneNames.EUROPE_WEST1_C, carbon_intensity=122),
    GCPZone(name=GCPZoneNames.EUROPE_WEST1_D, carbon_intensity=122),
    GCPZone(name=GCPZoneNames.EUROPE_WEST2_A, carbon_intensity=136),
    GCPZone(name=GCPZoneNames.EUROPE_WEST2_B, carbon_intensity=136),
    GCPZone(name=GCPZoneNames.EUROPE_WEST2_C, carbon_intensity=136),
    GCPZone(name=GCPZoneNames.EUROPE_WEST3_A, carbon_intensity=345),
    GCPZone(name=GCPZoneNames.EUROPE_WEST3_B, carbon_intensity=345),
    GCPZone(name=GCPZoneNames.EUROPE_WEST3_C, carbon_intensity=345),
    GCPZone(name=GCPZoneNames.EUROPE_WEST4_A, carbon_intensity=236),
    GCPZone(name=GCPZoneNames.EUROPE_WEST4_B, carbon_intensity=236),
    GCPZone(name=GCPZoneNames.EUROPE_WEST4_C, carbon_intensity=236),
    GCPZone(name=GCPZoneNames.EUROPE_WEST6_A, carbon_intensity=59),
    GCPZone(name=GCPZoneNames.EUROPE_WEST6_B, carbon_intensity=59),
    GCPZone(name=GCPZoneNames.EUROPE_WEST6_C, carbon_intensity=59),
    GCPZone(name=GCPZoneNames.EUROPE_WEST8_A, carbon_intensity=249),
    GCPZone(name=GCPZoneNames.EUROPE_WEST8_B, carbon_intensity=249),
    GCPZone(name=GCPZoneNames.EUROPE_WEST8_C, carbon_intensity=249),
    GCPZone(name=GCPZoneNames.EUROPE_WEST9_A, carbon_intensity=34),
    GCPZone(name=GCPZoneNames.EUROPE_WEST9_B, carbon_intensity=34),
    GCPZone(name=GCPZoneNames.EUROPE_WEST9_C, carbon_intensity=34),
    GCPZone(name=GCPZoneNames.EUROPE_WEST10_A, carbon_intensity=345),
    GCPZone(name=GCPZoneNames.EUROPE_WEST10_B, carbon_intensity=345),
    GCPZone(name=GCPZoneNames.EUROPE_WEST10_C, carbon_intensity=345),
    GCPZone(name=GCPZoneNames.EUROPE_WEST12_A, carbon_intensity=249),
    GCPZone(name=GCPZoneNames.EUROPE_WEST12_B, carbon_intensity=249),
    GCPZone(name=GCPZoneNames.EUROPE_WEST12_C, carbon_intensity=249),
    GCPZone(name=GCPZoneNames.EUROPE_SOUTHWEST1_A, carbon_intensity=131),
    GCPZone(name=GCPZoneNames.EUROPE_SOUTHWEST1_B, carbon_intensity=131),
    GCPZone(name=GCPZoneNames.EUROPE_SOUTHWEST1_C, carbon_intensity=131),
    # Asia
    GCPZone(name=GCPZoneNames.ASIA_EAST1_A, carbon_intensity=451),
    GCPZone(name=GCPZoneNames.ASIA_EAST1_B, carbon_intensity=451),
    GCPZone(name=GCPZoneNames.ASIA_EAST1_C, carbon_intensity=451),
    GCPZone(name=GCPZoneNames.ASIA_EAST2_A, carbon_intensity=360),
    GCPZone(name=GCPZoneNames.ASIA_EAST2_B, carbon_intensity=360),
    GCPZone(name=GCPZoneNames.ASIA_EAST2_C, carbon_intensity=360),
    GCPZone(name=GCPZoneNames.ASIA_NORTHEAST1_A, carbon_intensity=459),
    GCPZone(name=GCPZoneNames.ASIA_NORTHEAST1_B, carbon_intensity=459),
    GCPZone(name=GCPZoneNames.ASIA_NORTHEAST1_C, carbon_intensity=459),
    GCPZone(name=GCPZoneNames.ASIA_NORTHEAST2_A, carbon_intensity=385),
    GCPZone(name=GCPZoneNames.ASIA_NORTHEAST2_B, carbon_intensity=385),
    GCPZone(name=GCPZoneNames.ASIA_NORTHEAST2_C, carbon_intensity=385),
    GCPZone(name=GCPZoneNames.ASIA_NORTHEAST3_A, carbon_intensity=378),
    GCPZone(name=GCPZoneNames.ASIA_NORTHEAST3_B, carbon_intensity=378),
    GCPZone(name=GCPZoneNames.ASIA_NORTHEAST3_C, carbon_intensity=378),
    GCPZone(name=GCPZoneNames.ASIA_SOUTH1_A, carbon_intensity=648),
    GCPZone(name=GCPZoneNames.ASIA_SOUTH1_B, carbon_intensity=648),
    GCPZone(name=GCPZoneNames.ASIA_SOUTH1_C, carbon_intensity=648),
    GCPZone(name=GCPZoneNames.ASIA_SOUTH2_A, carbon_intensity=529),
    GCPZone(name=GCPZoneNames.ASIA_SOUTH2_B, carbon_intensity=529),
    GCPZone(name=GCPZoneNames.ASIA_SOUTH2_C, carbon_intensity=529),
    GCPZone(name=GCPZoneNames.ASIA_SOUTHEAST1_A, carbon_intensity=369),
    GCPZone(name=GCPZoneNames.ASIA_SOUTHEAST1_B, carbon_intensity=369),
    GCPZone(name=GCPZoneNames.ASIA_SOUTHEAST1_C, carbon_intensity=369),
    GCPZone(name=GCPZoneNames.ASIA_SOUTHEAST2_A, carbon_intensity=580),
    GCPZone(name=GCPZoneNames.ASIA_SOUTHEAST2_B, carbon_intensity=580),
    GCPZone(name=GCPZoneNames.ASIA_SOUTHEAST2_C, carbon_intensity=580),
    # Australia
    GCPZone(name=GCPZoneNames.AUSTRALIA_SOUTHEAST1_A, carbon_intensity=501),
    GCPZone(name=GCPZoneNames.AUSTRALIA_SOUTHEAST1_B, carbon_intensity=501),
    GCPZone(name=GCPZoneNames.AUSTRALIA_SOUTHEAST1_C, carbon_intensity=501),
    GCPZone(name=GCPZoneNames.AUSTRALIA_SOUTHEAST2_A, carbon_intensity=456),
    GCPZone(name=GCPZoneNames.AUSTRALIA_SOUTHEAST2_B, carbon_intensity=456),
    GCPZone(name=GCPZoneNames.AUSTRALIA_SOUTHEAST2_C, carbon_intensity=456),
    # South America
    GCPZone(name=GCPZoneNames.SOUTHAMERICA_EAST1_A, carbon_intensity=56),
    GCPZone(name=GCPZoneNames.SOUTHAMERICA_EAST1_B, carbon_intensity=56),
    GCPZone(name=GCPZoneNames.SOUTHAMERICA_EAST1_C, carbon_intensity=56),
    GCPZone(name=GCPZoneNames.SOUTHAMERICA_WEST1_A, carbon_intensity=138),
    GCPZone(name=GCPZoneNames.SOUTHAMERICA_WEST1_B, carbon_intensity=138),
    GCPZone(name=GCPZoneNames.SOUTHAMERICA_WEST1_C, carbon_intensity=138),
    # Africa
    GCPZone(name=GCPZoneNames.AFRICA_SOUTH1_A, carbon_intensity=646),
    GCPZone(name=GCPZoneNames.AFRICA_SOUTH1_B, carbon_intensity=646),
    GCPZone(name=GCPZoneNames.AFRICA_SOUTH1_C, carbon_intensity=646),
    # Middle East
    GCPZone(name=GCPZoneNames.ME_CENTRAL1_A, carbon_intensity=575),
    GCPZone(name=GCPZoneNames.ME_CENTRAL1_B, carbon_intensity=575),
    GCPZone(name=GCPZoneNames.ME_CENTRAL1_C, carbon_intensity=575),
    GCPZone(name=GCPZoneNames.ME_CENTRAL2_A, carbon_intensity=569),
    GCPZone(name=GCPZoneNames.ME_CENTRAL2_B, carbon_intensity=569),
    GCPZone(name=GCPZoneNames.ME_CENTRAL2_C, carbon_intensity=569),
    GCPZone(name=GCPZoneNames.ME_WEST1_A, carbon_intensity=463),
    GCPZone(name=GCPZoneNames.ME_WEST1_B, carbon_intensity=463),
    GCPZone(name=GCPZoneNames.ME_WEST1_C, carbon_intensity=463),
]

ZONES_BY_NAME: dict[GCPZoneNames, GCPZone] = {zone.name: zone for zone in ZONES}

GPUS: list[GCPGPU] = [
    GCPGPU(name=GCPGPUNames.NVIDIA_TESLA_P100, efficiency=15.7),
    GCPGPU(name=GCPGPUNames.NVIDIA_V100, efficiency=26.0),
    GCPGPU(name=GCPGPUNames.NVIDIA_A100_40GB, efficiency=38.8),
    GCPGPU(name=GCPGPUNames.NVIDIA_A100_80GB, efficiency=48.8),
    GCPGPU(name=GCPGPUNames.NVIDIA_H100_80GB, efficiency=85.7),
    GCPGPU(name=GCPGPUNames.NVIDIA_H100_80GB_MEGA, efficiency=85.7),
    GCPGPU(name=GCPGPUNames.NVIDIA_T4, efficiency=116.0),
    GCPGPU(name=GCPGPUNames.NVIDIA_L4, efficiency=210.0),
    GCPGPU(name=GCPGPUNames.NVIDIA_TESLA_P4, efficiency=73.3),
    GCPGPU(name=GCPGPUNames.NVIDIA_H200_141GB, efficiency=48.57),
]

GPUS_BY_NAME: dict[GCPGPUNames, GCPGPU] = {gpu.name: gpu for gpu in GPUS}
