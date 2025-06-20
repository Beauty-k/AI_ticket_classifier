from utils.text_transformer_interface import TextTransformer

class SpecialCharRemover(TextTransformer):
    
    def transform(self, text):
        return ''.join(ch if ch.isalnum() or ch.isspace() else '' for ch in text)