from abc import ABC, abstractmethod

class EntityExtractor(ABC):
    @abstractmethod
    def extract(self, text: str) -> dict:
        pass