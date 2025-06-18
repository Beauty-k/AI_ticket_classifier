from utils.lowercaser import Lowercaser
from utils.special_char_remover import SpecialCharRemover
from utils.lemmatizer import Lemmatizer

class TextPreprocessor:
    def __init__(self):
        self.pipeline = [
            Lowercaser(),
            SpecialCharRemover(),
            Lemmatizer()
        ]

    def preprocess(self, text: str) -> str:
        for transformer in self.pipeline:
            text = transformer.tranform(text)
        return text

    def transform_series(self, series):
        return series.astype(str).apply(self.preprocess)
