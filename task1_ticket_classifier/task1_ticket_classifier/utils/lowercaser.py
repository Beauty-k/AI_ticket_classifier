from utils.text_transformer_interface import TextTransformer

class Lowercaser(TextTransformer):

    def transform(self, text):
        return text.lower()