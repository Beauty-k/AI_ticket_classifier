from utils.quote_data_loader import QuoteDataLoader
from models.quote_embedder import QuoteEmbedder
import os

# Create models directory if it doesn't exist
os.makedirs("models", exist_ok=True)

# Load quotes
loader = QuoteDataLoader()
quotes = loader.load_quotes()

# Encode and save
embedder = QuoteEmbedder()
embeddings = embedder.encode_quotes(quotes)
embedder.save_embeddings(embeddings, quotes)

print("Embeddings and quotes saved!")