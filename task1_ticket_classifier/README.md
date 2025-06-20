**Internship Assignment – Vijayi WFH Technologies**  
**Task 1: Ticket Classification and Entity Extraction**

# Introduction

This project implements a modular machine learning pipeline to:

- Classify support tickets by:
  - Issue Type (e.g., Billing Problem, Product Defect)
  - Urgency Level (High, Medium, Low)
- Extract key entities from ticket text:
  - Product names
  - Dates
  - Complaint keywords

Implemented fully in Python using object-oriented programming (OOP), interface-based design, and clean coding practices.


# Implementation Steps

### 1. Data Preparation

- Loaded Excel file using pandas
- Cleaned and normalized `ticket_text`:
  - Lowercased
  - Special characters removed
  - Lemmatized (using spaCy)
- Used a custom preprocessing pipeline:
  - `Lowercaser`
  - `SpecialCharRemover`
  - `Lemmatizer`

### 2. Feature Engineering

Three feature extractors:

- `TfidfEngineer`: TF-IDF vector (top 1000 features)
- `LengthEngineer`: Ticket length (number of characters)
- `SentimentEngineer`: Sentiment polarity using TextBlob

All features are combined using `FeatureCombiner`.

### 3. Multi-Task Classification

Two models trained:

- `issue_type_classifier.pkl` → predicts `issue_type`
- `urgency_level_classifier.pkl` → predicts `urgency_level`

Both use `RandomForestClassifier` and implement the `Classifier` interface.

Performance metrics are printed using `classification_report`.

### 4. Entity Extraction

Rule-based NLP methods (no LLMs used):

- Product names (from list)
- Dates (via regex)
- Complaint keywords (from static list)

Class used: `RuleBasedEntityExtractor` implementing `EntityExtractor`.

### 5. Integration

All logic integrated into a single reusable class:

TicketProcessor().process(text)
This returns:-
    {
        "issue_type": issue_type,
        "urgency_level": urgency_level,
        "entities": entities
    }


# Project Structure

- task1_ticket_classifier/
    ─ models/                    # Saved models and vectorizer
    ─ data/                      # Input Excel file
    ─ components/                # Modular OOP structure
    ─ text_transforms/           # Preprocessors
    ─ features/                  # Feature extractors
    ─ models/                    # Classifier implementations
    ─ entity_extractors/         # Rule-based extractor
    ─ inference/                 # Final integration logic
    ─ train_models.py            # Model training
    ─ predict_ticket.py          # Inference
    ─ README.md 

# Key Design Choices
- Followed Object-Oriented Programming and the Single Responsibility Principle to ensure modular, testable, and 
  extensible code.
- Used interfaces (abstract base classes) to allow easy swapping of models, preprocessors, or feature extractors.
- Chose Random Forest for its robustness and interpretability in multi-class classification tasks.
- Applied traditional rule-based NLP for entity extraction — as required by the assignment.
   
#  Limitations 
- The urgency level classifier is not very accurate. This is likely because the labels like High, Medium, and Low  
  are subjective and not clearly defined in the data.
- The entity extractor is based on simple rules. It may miss spelling mistakes or similar words. For example, it 
  catches “broken” but not “damaged”
- It only detects dates in numeric format like 12/06/2025. It doesn’t handle words like “yesterday” or “last week”.
- Sentiment and length are basic features. The system could improve by using more advanced text features in the 
  future.