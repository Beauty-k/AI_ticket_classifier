import pandas as pd

class TicketDataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        df = pd.read_excel(self.filepath)
        return df