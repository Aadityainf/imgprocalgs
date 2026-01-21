from abc import ABC, abstractmethod
from PIL import Image

class BaseAlgorithm(ABC):
    def __init__(self, image=None):
        self.image = image

    def load_image(self, path):
        self.image = Image.open(path)
        return self.image

    @abstractmethod
    def compute(self, *args, **kwargs):
        """All algorithms must implement this method."""
        pass