from components.models.classifier_interface import Classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

class RandomForestTicketClassifier(Classifier):
    def __init__(self):
        self.model = RandomForestClassifier()
    
    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    
    def evaluate(self, X, y):
        y_pred = self.predict(X)
        print("Evaluation Report:\n")
        print(classification_report(y, y_pred))

    def save(self, path):
        joblib.dump(self.model, path)

    
    def load(self, path):
        self.model = joblib.load(path)