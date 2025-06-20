from sklearn.feature_extraction.text import TfidfVectorizer
from components.features.feature_engineer_interface import FeatureEngineer
import joblib

class TfidfEngineer(FeatureEngineer):
    def __init__(self, max_features=1000):
        self.vectorizer = TfidfVectorizer(max_features=max_features)
    
    def extract(self, df):
        X = self.vectorizer.fit_transform(df["clean_text"])
        joblib.dump(self.vectorizer, "models/tfidf_vectorizer.pkl")
        return X