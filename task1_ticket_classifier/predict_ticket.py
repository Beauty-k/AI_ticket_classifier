from components.entity_extractors.rule_based_entity_extractor import RuleBasedEntityExtractor
import pandas as pd
from components.inference.ticket_processor import TicketProcessor
import joblib


df = pd.read_excel("data/ai_dev_assignment_tickets_complex_1000.xls")
# Get product list from your dataset
product_list = df["product"].dropna().unique().tolist()
joblib.dump(product_list, "models/product_list.pkl")

extractor = RuleBasedEntityExtractor(product_list)

processor = TicketProcessor()

text = "My laptop arrived cracked on 12/06/2025 and it's not working. This is urgent."
entities = extractor.extract(text)

result = processor.process(text)

print(entities)
print(result)

