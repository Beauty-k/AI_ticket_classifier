
from datasets import load_dataset

class QuoteDataLoader:
    # def __init__(self, dataset_name="sberbank-ai/russian-quotes", split="train"):
    #     self.dataset_name = dataset_name
    #     self.split = split

    def load_quotes(self):
        # dataset = load_dataset(self.dataset_name, split=self.split)
        # return [item["quote"] for item in dataset if "quote" in item]
        return [
            "Success is not final, failure is not fatal: It is the courage to continue that counts.",
            "Believe you can and you're halfway there.",
            "It always seems impossible until it's done.",
            "Start where you are. Use what you have. Do what you can.",
            "The only way to do great work is to love what you do.",
            "Don’t watch the clock; do what it does. Keep going.",
            "Hardships often prepare ordinary people for an extraordinary destiny.",
            "You are never too old to set another goal or to dream a new dream."
        ]