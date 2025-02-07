import boto3
import json
from botocore.exceptions import ClientError
from .base import CloudProvider  

class AWSCloudProvider(CloudProvider):
    def __init__(self, region):
        super().__init__("AWS")
        self.region = region
        self.ec2_client = boto3.client("ec2", region_name=region)


    def fetch_gpu_available(self):
        """
        Query EC2 to list all instance types that include GPU accelerators.
        AWS returns GPU information in the 'GpuInfo' field.
        """
        available_gpus = []
        paginator = self.ec2_client.get_paginator("describe_instance_types")
        for page in paginator.paginate():
            for instance in page.get("InstanceTypes", []):
                if "GpuInfo" in instance:
                    available_gpus.append({
                        "InstanceType": instance["InstanceType"],
                        "GpuInfo": instance["GpuInfo"]
                    })
        return available_gpus