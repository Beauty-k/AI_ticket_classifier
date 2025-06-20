import re
from components.entity_extractors.entity_extractor_interface import EntityExtractor

class RuleBasedEntityExtractor(EntityExtractor):
    def __init__(self, product_list):
        self.product_list = [p.lower() for p in product_list]
        self.complaint_keywords = ["broken", "late", "error", "missing", "cracked", "not working", "failed"]

    def extract(self, text: str) -> dict:
        text_lower = text.lower()

        products = [p for p in self.product_list if p.lower() in text_lower]
        dates = re.findall(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b', text)

        keywords = [k for k in self.complaint_keywords if k in text_lower]

        return {
            "product": products,
            "dates": dates,
            "keywords": keywords
        }