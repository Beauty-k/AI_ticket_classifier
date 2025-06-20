**Internship Assignment – Vijayi WFH Technologies**  
**Task 1: Ticket Classification and Entity Extraction**

# Introduction

This project builds a simple `quote suggestion system` using semantic similarity.

- Input: A user query (e.g., motivation for exams)
- Output: Top 3 most relevant quotes from a dataset
- Implemented using:
  - Sentence Transformers
  - Cosine similarity
  - Object-oriented, modular code (OOP)


## Implementation Steps

### 1. Dataset

- A custom local dataset (`quotes.csv`) is used with one column: `quote`
- Loaded using `pandas` in `QuoteDataLoader`

### 2. Embedding Creation

- Quotes are converted into vector embeddings using `all-MiniLM-L6-v2` from `sentence-transformers`
- Embeddings are stored in `models/quote_embeddings.npy`
- The raw quote texts are stored in `models/quotes_list.pkl`
- Script: `build_embeddings.py`


### 3. Retrieval Logic

- When a user inputs a query:
  - The system encodes the query using the same sentence transformer model
  - Calculates **cosine similarity** between the query and all quotes
  - Returns top 3 quotes with the highest similarity scores

- Retrieval is handled by `QuoteRetriever` class in `utils/quote_retriever.py`

### 4. Running the App

- Script: `predict_quote.py`
- Prompts the user for a search query and prints the most relevant quotes.

## Key Design Choices

- Used **sentence-transformers** to get meaningful semantic embeddings
- Followed **OOP principles**: loaders and retrievers are modular
- Used **cosine similarity** to measure closeness of meaning
- Made independent dataset:`quotes.csv`
(As my computer was not getting access to the given quotes platform link)

## Example Output

**User Input:** `motivation for exams`

Top Matching Quotes:
1. Failure will never overtake me if my determination to succeed is strong enough.
2. Dream big and dare to fail.
3. Success is not final, failure is not fatal: It is the courage to continue that counts.

## How to Run This Project
1. Set up Environment
- Install all dependencies:
    `pip install -r requirements.txt`
2. Prepare the Quotes
    ``data/quotes.csv``
3. Build Embeddings
   `python build_embeddings.py`
4. Run the App
    `python predict_quote.py`
- Type a query like:
    **motivation for failure**

## Project Structure
task2_quote_retriever/
    ─ data/
       ─ quotes.csv               # Custom dataset of quotes
    ─ models/
        ─ quote_embeddings.npy     # Vector embeddings
        ─ quotes_list.pkl          # Original quotes
    ─ utils/
        ─ quote_data_loader.py     # Loads dataset
        ─ quote_retriever.py       # Core retrieval logic
    ─ build_embeddings.py          # Preprocessing script
    ─ predict_quote.py             # Inference script
    ─ requirements.txt             # All dependencies
    ─ README.md

## Limitations
- Results depend heavily on quality and diversity of quotes.csv
- Cannot return quotes outside the dataset (not generative)
- Doesn’t handle language beyond English
- No Gradio/Web UI — this is CLI-only for now  
**Task 2 is partially implemented as a minimal version using semantic retrieval and cosine similarity.Full    RAG-based pipeline is in progress but not complete at the time of submission.** 
