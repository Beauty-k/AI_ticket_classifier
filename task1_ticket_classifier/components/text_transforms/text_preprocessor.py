from components.text_transforms.lowercaser import Lowercaser
from components.text_transforms.special_char_remover import SpecialCharRemover
from components.text_transforms.lemmatizer import Lemmatizer

class TextPreprocessor:
    def __init__(self):
        self.pipeline = [
            Lowercaser(),
            SpecialCharRemover(),
            Lemmatizer()
        ]

    def preprocess(self, text: str) -> str:
        for transformer in self.pipeline:
            text = transformer.transform(text)
        return text

    def transform_series(self, series):
        return series.astype(str).apply(self.preprocess)
