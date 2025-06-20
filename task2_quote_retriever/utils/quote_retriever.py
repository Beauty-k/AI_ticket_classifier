from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class QuoteRetriever:
    def __init__(self, quotes, embeddings, model):
        self.quotes = quotes
        self.embeddings = embeddings
        self.model = model

    def retrieve(self, query, top_k=3):
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        top_indices = similarities.argsort()[::-1][:top_k]
        return [self.quotes[i] for i in top_indices]
