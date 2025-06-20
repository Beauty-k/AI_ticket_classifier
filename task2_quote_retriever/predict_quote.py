import joblib
import numpy as np
from sentence_transformers import SentenceTransformer
from utils.quote_retriever import QuoteRetriever

quotes = joblib.load("models/quotes_list.pkl")
embeddings = np.load("models/quote_embeddings.npy")
model = SentenceTransformer("all-MiniLM-L6-v2")

retriever = QuoteRetriever(quotes, embeddings, model)

print("Ask for a quote!")
query = input("Enter your query: ")
results = retriever.retrieve(query)

print("Top Matching Quotes\n:")
for i, quote in enumerate(results, 1):
    print(f"{i}. {quote}")
