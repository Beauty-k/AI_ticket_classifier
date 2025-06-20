import pandas as pd
from components.text_transforms.text_preprocessor import TextPreprocessor
from components.features.tfidf_engineer import TfidfEngineer
from components.features.length_engineer import LengthEngineer
from components.features.sentiment_engineer import SentimentEngineer
from components.features.feature_combiner import FeatureCombiner

# Load your data
df = pd.read_excel("data/ai_dev_assignment_tickets_complex_1000.xls")
print("data frame",df)
# Preprocess
tp = TextPreprocessor()
df['clean_text'] = tp.transform_series(df['ticket_text'])

# Feature engineering
engineers = [TfidfEngineer(), LengthEngineer(), SentimentEngineer()]
fc = FeatureCombiner(engineers)
X = fc.combine(df)