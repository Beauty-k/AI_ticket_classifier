from sentence_transformers import SentenceTransformer
import numpy as np
import joblib

class QuoteEmbedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode_quotes(self, quotes):
        embeddings = self.model.encode(quotes, show_progress_bar=True)
        return np.array(embeddings)

    def save_embeddings(self, embeddings, quotes, embed_path="models/quote_embeddings.npy", quote_path="models/quotes.pkl"):
        np.save(embed_path, embeddings)
        joblib.dump(quotes, quote_path)

    def load_embeddings(self, embed_path="models/quote_embeddings.npy", quote_path="models/quotes.pkl"):
        embeddings = np.load(embed_path)
        quotes = joblib.load(quote_path)
        return embeddings, quotes