import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import joblib

class QuoteRetriever:
    def __init__(self, embed_path="models/quote_embeddings.npy", quote_path="models/quotes.pkl", model_name="all-MiniLM-L6-v2"):
        self.embeddings = np.load(embed_path)
        self.quotes = joblib.load(quote_path)
        self.model = SentenceTransformer(model_name)

    def retrieve(self, query, top_k=3):
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        top_indices = similarities.argsort()[::-1][:top_k]
        results = [self.quotes[i] for i in top_indices]
        return results