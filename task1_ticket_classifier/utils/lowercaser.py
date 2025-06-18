from utils.text_transformer import TextTransformer

class Lowercaser(TextTransformer):

    def transform(self, text):
        return text.lower()