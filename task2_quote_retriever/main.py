from utils.quote_data_loader import QuoteDataLoader
from models.quote_embedder import QuoteEmbedder
from utils.quote_retriever import QuoteRetriever


# Load quotes
loader = QuoteDataLoader()
quotes = loader.load_quotes()

# Encode and save
embedder = QuoteEmbedder()
embeddings = embedder.encode_quotes(quotes)
embedder.save_embeddings(embeddings, quotes)

retriever = QuoteRetriever()
results = retriever.retrieve("I need motivation for exams", top_k=3)

for quote in results:
    print("-", quote)