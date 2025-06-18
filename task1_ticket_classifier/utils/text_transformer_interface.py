from abc import ABC, abstractmethod

class TextTransformer(ABC):
    @abstractmethod
    def transform(self, text):
        pass
    