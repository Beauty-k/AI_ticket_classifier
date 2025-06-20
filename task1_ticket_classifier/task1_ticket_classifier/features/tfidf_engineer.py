from sklearn.feature_extraction.text import TfidfVectorizer
from features.feature_engineer_interface import FeatureEngineer

class TfidfEngineer(FeatureEngineer):
    def __init__(self, max_features=1000):
        self.vectorizer = TfidfVectorizer(max_features=max_features)
    
    def extract(self, df):
        return self.vectorizer.fit_transform(df["clean_text"])