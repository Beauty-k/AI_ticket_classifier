import joblib
from components.text_transforms.text_preprocessor import TextPreprocessor
from components.entity_extractors.rule_based_entity_extractor import RuleBasedEntityExtractor
from textblob import TextBlob

class TicketProcessor:
    def __init__(self):
        # Load trained models
        self.issue_model = joblib.load("models/issue_type_classifier.pkl")
        self.urgency_model = joblib.load("models/urgency_level_classifier.pkl")
        self.vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

        # Load product list
        self.product_list = joblib.load("models/product_list.pkl")
        self.extractor = RuleBasedEntityExtractor(self.product_list)
        self.preprocessor = TextPreprocessor()

    def process(self, text: str) -> dict:
        # Preprocess text
        clean_text = self.preprocessor.preprocess(text)

        # Feature extraction
        X_text = self.vectorizer.transform([clean_text])
        length = [[len(text)]]
        sentiment = [[TextBlob(text).sentiment.polarity]]

        from scipy.sparse import hstack
        X = hstack([X_text, length, sentiment])

        # Predictions
        issue_type = self.issue_model.predict(X)[0]
        urgency_level = self.urgency_model.predict(X)[0]

        # Entity extraction
        entities = self.extractor.extract(text)

        return {
            "issue_type": issue_type,
            "urgency_level": urgency_level,
            "entities": entities
        }