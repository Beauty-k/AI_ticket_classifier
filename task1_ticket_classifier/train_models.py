import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
from sklearn.model_selection import train_test_split
from components.text_transforms.text_preprocessor import TextPreprocessor
from components.models.random_forest_classifier import RandomForestTicketClassifier
from textblob import TextBlob


# Load the dataset
df = pd.read_excel("data/ai_dev_assignment_tickets_complex_1000.xls")

# Load and preprocess
preprocessor = TextPreprocessor()
df["clean_text"] = preprocessor.transform_series(df["ticket_text"])

df = df.dropna(subset=["issue_type", "urgency_level"])

# Load vectorizer and features
vectorizer = TfidfVectorizer(max_features=1000)
vectorizer.fit(df["clean_text"])
joblib.dump(vectorizer, "models/tfidf_vectorizer.pkl")
X_text = vectorizer.transform(df['clean_text'])

# Load extra features
lengths = df['ticket_text'].astype(str).apply(len).values.reshape(-1, 1)

sentiment = df['ticket_text'].astype(str).apply(
    lambda x: TextBlob(x).sentiment.polarity).values.reshape(-1, 1)

# Combine all features (same logic as before)
import numpy as np
from scipy.sparse import hstack
X = hstack([X_text, lengths, sentiment])

# 1. Issue Type Classifier
X_train_i, X_test_i, y_train_i, y_test_i = train_test_split(
    X, df['issue_type'], test_size=0.2, random_state=42
)

issue_model = RandomForestTicketClassifier()
issue_model.train(X_train_i, y_train_i)
issue_model.evaluate(X_test_i, y_test_i)
issue_model.save("models/issue_type_classifier.pkl")

# 2. Urgency Level Classifier
X_train_u, X_test_u, y_train_u, y_test_u = train_test_split(
    X, df['urgency_level'], test_size=0.2, random_state=42
)

urgency_model = RandomForestTicketClassifier()
urgency_model.train(X_train_u, y_train_u)
urgency_model.evaluate(X_test_u, y_test_u)
urgency_model.save("models/urgency_level_classifier.pkl")