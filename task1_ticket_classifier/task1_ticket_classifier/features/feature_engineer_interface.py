from abc import ABC, abstractmethod

class FeatureEngineer(ABC):
    @abstractmethod
    def extract(self, df):
        pass