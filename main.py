import os
from cloud_providers import GoogleCloudProvider, AWSCloudProvider, AzureCloudProvider
from dotenv import load_dotenv
import json

# https://gist.github.com/ausfestivus/04e55c7d80229069bf3bc75870630ec8
ZONES_AZURE = [
    "eastus", "eastus2", "southcentralus", "westus2",
    "westus3", "australiaeast", "southeastasia",
    "northeurope", "swedencentral", "uksouth",
    "westeurope", "centralus", "southafricanorth",
    "centralindia", "eastasia", "japaneast", "koreacentral",
    "canadacentral", "francecentral", "germanywestcentral",
    "italynorth", "norwayeast", "polandcentral", "spaincentral",
    "switzerlandnorth", "mexicocentral", "uaenorth", "brazilsouth",
    "israelcentral", "qatarcentral", "centralusstage", "eastusstage",
    "eastus2stage", "northcentralusstage", "southcentralusstage",
    "westusstage", "westus2stage", "brazilus", "eastusstg",
    "northcentralus", "westus", "japanwest", "jioindiawest",
    "centraluseuap", "eastus2euap", "westcentralus", "southafricawest",
    "australiacentral", "australiacentral2", "australiasoutheast",
    "jioindiacentral", "koreasouth", "southindia", "westindia",
    "canadaeast", "francesouth", "germanynorth", "norwaywest",
    "switzerlandwest", "ukwest", "uaecentral", "brazilsoutheast"
]


ZONES_AWS = [
    "us-east-2", "us-east-1", "us-west-1", "us-west-2",
    "af-south-1", "ap-east-1", "ap-south-2", "ap-southeast-3",
    "ap-southeast-5", "ap-southeast-4", "ap-south-1",
    "ap-northeast-3", "ap-northeast-2", "ap-southeast-1",
    "ap-southeast-2", "ap-southeast-7", "ap-northeast-1",
    "ca-central-1", "ca-west-1", "eu-central-1", "eu-west-1",
    "eu-west-2", "eu-west-3", "eu-south-2",
    "eu-north-1", "eu-central-2", "mx-central-1",
    "me-south-1", "me-central-1", "sa-east-1", "us-gov-east-1",
]

# https://cloud.google.com/compute/docs/regions-zones
ZONES_GCP = [
    "us-central1-a", "us-central1-b", "us-central1-c", "us-central1-f",

    "us-east1-b", "us-east1-c", "us-east1-d",
    "us-east4-a", "us-east4-b", "us-east4-c", 
    "us-east5-a", "us-east5-b", "us-east5-c",

    "us-west1-a", "us-west1-b", "us-west1-c",
    "us-west2-a", "us-west2-b", "us-west2-c",
    "us-west3-a", "us-west3-b", "us-west3-c",
    "us-west4-a", "us-west4-b", "us-west4-c",

    "northamerica-northeast1-a", "northamerica-northeast1-b",
    "northamerica-northeast1-c", "northamerica-northeast2-a",
    "northamerica-northeast2-b", "northamerica-northeast2-c",
    "northamerica-south1-a", "northamerica-south1-b", "northamerica-south1-c",

    "us-south1-a", "us-south1-b", "us-south1-c",

    "europe-north1-a", "europe-north1-b", "europe-north1-c",
    "europe-central2-a", "europe-central2-b", "europe-central2-c",

    "europe-southwest1-a", "europe-southwest1-b", "europe-southwest1-c",

    "europe-west1-b", "europe-west1-c", "europe-west1-d",
    "europe-west2-a", "europe-west2-b", "europe-west2-c",
    "europe-west3-a", "europe-west3-b", "europe-west3-c",
    "europe-west4-a", "europe-west4-b", "europe-west4-c",
    "europe-west6-a", "europe-west6-b", "europe-west6-c",
    "europe-west8-a", "europe-west8-b", "europe-west8-c",
    "europe-west9-a", "europe-west9-b", "europe-west9-c",
    "europe-west10-a", "europe-west10-b", "europe-west10-c",
    "europe-west12-a", "europe-west12-b", "europe-west12-c",

    "asia-east1-a", "asia-east1-b", "asia-east1-c",
    "asia-east2-a", "asia-east2-b", "asia-east2-c",

    "asia-northeast1-a", "asia-northeast1-b", "asia-northeast1-c",
    "asia-northeast2-a", "asia-northeast2-b", "asia-northeast2-c",
    "asia-northeast3-a", "asia-northeast3-b", "asia-northeast3-c",

    "asia-south1-a", "asia-south1-b", "asia-south1-c",
    "asia-south2-a", "asia-south2-b", "asia-south2-c",
    "asia-southeast1-a", "asia-southeast1-b", "asia-southeast1-c",
    "asia-southeast2-a", "asia-southeast2-b", "asia-southeast2-c",

    "australia-southeast1-a", "australia-southeast1-b", "australia-southeast1-c",
    "australia-southeast2-a", "australia-southeast2-b", "australia-southeast2-c",

    "southamerica-east1-a", "southamerica-east1-b",
    "southamerica-east1-c", "southamerica-west1-a",
    "southamerica-west1-b", "southamerica-west1-c",

    "africa-south1-a", "africa-south1-b", "africa-south1-c",

    "me-central1-a", "me-central1-b", "me-central1-c",
    "me-central2-a", "me-central2-b", "me-central2-c",
    "me-west1-a", "me-west1-b", "me-west1-c"
]

# https://cloud.google.com/sustainability/region-carbon
GCP_intensity = {
    'africa-south1': 646,
    'asia-east1': 451,
    'asia-east2': 360,
    'asia-northeast1': 459,
    'asia-northeast2': 385,
    'asia-northeast3': 378,
    'asia-south1': 648,
    'asia-south2': 529,
    'asia-southeast1': 369,
    'asia-southeast2': 580,
    'australia-southeast1': 501,
    'australia-southeast2': 456,
    'europe-central2': 723,
    'europe-north1': 46,
    'europe-southwest1': 131,
    'europe-west1': 122,
    'europe-west2': 136,
    'europe-west3': 345,
    'europe-west4': 236,
    'europe-west6': 59,
    'europe-west8': 249,
    'europe-west9': 34,
    'europe-west10': 345,
    'europe-west12': 249,
    'me-central1': 575,
    'me-central2': 569,
    'me-west1': 463,
    'northamerica-northeast1': 2,
    'northamerica-northeast2': 47,
    'southamerica-east1': 56,
    'southamerica-west1': 138,
    'us-central1': 430,
    'us-east1': 560,
    'us-east4': 322,
    'us-east5': 322,
    'us-south1': 321,
    'us-west1': 94,
    'us-west2': 198,
    'us-west3': 588,
    'us-west4': 373
}

GPU_efficiency = {
    "NVIDIA Tesla P100": 15.7, "NVIDIA V100": 26, 
    "NVIDIA A100 40GB": 38.8, "NVIDIA A100 80GB": 48.8, 
    "NVIDIA H100 80GB": 85.7, "NVIDIA H100 80GB MEGA": 85.7,
    "NVIDIA T4": 116, "NVIDIA L4": 210, "NVIDIA Tesla P4": 73.3,
    "NVIDIA H200 141GB": 48.57
}


def save_to_json(filename, data):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
        print(f"Saved data to {filename}")

# load environment variables
load_dotenv()
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCP_SERVICE_ACCOUNT_FILE = os.getenv("GCP_SERVICE_ACCOUNT_FILE")

# instanciate cloud providers
GCP = GoogleCloudProvider(GCP_PROJECT_ID, GCP_SERVICE_ACCOUNT_FILE)
AWS = AWSCloudProvider(ZONES_AWS)

# fetch available GPUs
gcp_gpu_available = GCP.fetch_gpu_available(ZONES_GCP)
gcp_gpu_pricing = GCP.fetch_gpu_pricing()
save_to_json("jsons/gcp_gpu_available.json", gcp_gpu_pricing)

for gpu in gcp_gpu_available:
    gpu["Carbon intensity (gCO2eq/kWh)"] = GCP_intensity[gpu["Zone"].rsplit("-", 1)[0]] 
    gpu["Energy Efficiency [GFlops/Watts]"] = GPU_efficiency[gpu["Description"]] 
    gpu["Zone"] = GCP_intensity[gpu["Zone"].rsplit("-", 1)[0]]
    # gpu["Price (USD/hour)"] = gcp_gpu_pricing[(Zone, Description)]

save_to_json("jsons/gcp_gpu_available.json", gcp_gpu_available)

#aws_gpu_available = AWS.fetch_gpu_available()
#for gpu in aws_gpu_available:
#    gpu["Carbon intensity (gCO2eq/kWh)"] = GCP_intensity[gpu["Zone"].rsplit("-", 1)[0]] 
#    gpu["Energy Efficiency [GFlops/Watts]"] = GPU_efficiency[gpu["Description"]] 
#save_to_json("jsons/aws_gpu_available.json", aws_gpu_available)

#gcp_gpu_pricing = GCP.fetch_gpu_pricing()
#save_to_json("jsons/gcp_gpu_pricing.json", gcp_gpu_pricing)
"""
for device in list1:
    description = device.get("Description")
    if description in energy_efficiency_dict:
        device["energy efficiency"] = energy_efficiency_dict[description]
    else:
        device["energy efficiency"] = None  # or handle missing values as needed
"""