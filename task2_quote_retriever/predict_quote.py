from utils.quote_retriever import QuoteRetriever

if __name__ == "__main__":
    retriever = QuoteRetriever()

    print("Ask for a quote! Type something like:\n")
    print("  - 'motivation for exams'")
    print("  - 'quote on failure'")
    print("  - 'something positive'\n")

    query = input("Enter your query: ")
    top_quotes = retriever.retrieve(query, top_k=3)

    print("\n🔍 Top Matching Quotes:")
    for i, quote in enumerate(top_quotes, 1):
        print(f"{i}. {quote}")