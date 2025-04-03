from .base import CloudProvider

class AzureCloudProvider(CloudProvider):
    def __init__(self, name):
        self.name = name

    def fetch_gpu_available(self):
        pass

    def fetch_gpu_pricing(self):
        pass

    def preprocess_gpu(self):
        pass
