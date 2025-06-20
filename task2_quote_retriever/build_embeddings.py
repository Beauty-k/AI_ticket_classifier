from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from utils.quote_data_loader import QuoteDataLoader
import joblib

model = SentenceTransformer("all-MiniLM-L6-v2")
loader = QuoteDataLoader()
quotes = loader.load_quotes()
embeddings = model.encode(quotes)

np.save("models/quote_embeddings.npy", embeddings)
joblib.dump(quotes, "models/quotes_list.pkl")
print(f"Quotes loaded: {len(quotes)}")
