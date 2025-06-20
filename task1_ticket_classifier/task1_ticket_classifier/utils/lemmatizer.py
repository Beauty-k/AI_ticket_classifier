import spacy
from utils.text_transformer_interface import TextTransformer

class Lemmatizer(TextTransformer):
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def transform(self, text):
        doc = self.nlp(text) 
        tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
        return ' '.join(tokens)