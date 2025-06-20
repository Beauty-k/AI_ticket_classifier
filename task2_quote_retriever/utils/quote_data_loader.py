import pandas as pd

class QuoteDataLoader:
    def __init__(self, file_path="data/quotes.csv"):
        self.file_path = file_path

    def load_quotes(self):
        df = pd.read_csv(self.file_path)
        return df['quote'].dropna().tolist()