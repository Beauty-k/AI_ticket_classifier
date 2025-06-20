from textblob import TextBlob
from features.feature_engineer_interface import FeatureEngineer


class SentimentEngineer(FeatureEngineer):
    def extract(self, df):
        return df['ticket_text'].astype(str).apply(lambda x: TextBlob(x).sentiment.polarity).values.reshape(-1, 1)
    