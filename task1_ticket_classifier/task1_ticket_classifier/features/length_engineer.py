from features.feature_engineer_interface import FeatureEngineer

class LengthEngineer(FeatureEngineer):
    def extract(self, df):
        return df['ticket_text'].astype(str).apply(len).values.reshape(-1, 1)