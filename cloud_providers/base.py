from abc import ABC, abstractmethod


class CloudProvider(ABC):
    """Abstract class for creating cloud provider gpu fetching class"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fetch_gpu_available(self):
        """Query and preprocess endpoint with available GPUs"""
        pass

    @abstractmethod
    def fetch_gpu_pricing(self):
        """Query and preprocess GPUs pricing data"""
        pass

    @abstractmethod
    def preprocess_gpu(self):
        """Helper method for preprocessing gpu data"""
        pass
