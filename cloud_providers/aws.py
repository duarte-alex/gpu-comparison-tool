import boto3
import json
from botocore.exceptions import ClientError
from .base import CloudProvider  

class AWSCloudProvider(CloudProvider):
    def __init__(self, regions):
        super().__init__("AWS")
        self.regions = regions

    def fetch_gpu_available(self):
        available_gpus = []
        for region in self.regions:
            print(region)
            ec2_client = boto3.client("ec2", region_name=region)
            paginator = ec2_client.get_paginator("describe_instance_types")
            for page in paginator.paginate():
                for instance in page.get("InstanceTypes", []):
                    if "GpuInfo" in instance:
                        GpuInfo = instance["GpuInfo"]["Gpus"][0]
                        available_gpus.append({
                            "Zone": region,
                            "Description": GpuInfo["Manufacturer"] + " " + GpuInfo["Name"]
                        })
        return available_gpus

    
    def fetch_gpu_pricing(self):
        """Query and preprocess GPUs pricing data"""
        pass

    def preprocess_gpu(self):
        """Helper method for preprocessing gpu data"""
        pass