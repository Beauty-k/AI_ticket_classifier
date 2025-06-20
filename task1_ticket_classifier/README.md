<<<<<<< HEAD
# AI_ticket_classifier
=======

**Internship Assignment – Vijayi WFH Technologies (June 2025)**
**Task 1: Ticket Classification and Entity Extraction**

## Overview
This project implements a modular machine learning pipeline to:

- Classify support tickets by:
  - Issue Type (ex., Billing Problem, Product Defect)
  - Urgency Level (High, Medium, Low)
- Extract key entities from ticket text:
  - Product names
  - Dates
  - Complaint keywords

  Implemented fully in Python using object-oriented programming (OOP), interface-based design, and clean coding practices.

  ## Implementation steps:-

### 1. Data Preparation

- Loaded Excel file using pandas
- Cleaned and normalized `ticket_text`:
  - Lowercased
  - Special characters removed
  - Lemmatized (using spaCy)
- Used OOP-based preprocessing pipeline:
  - `Lowercaser`
  - `SpecialCharRemover`
  - `Lemmatizer`

  ### 2. Feature Engineering

Three independent feature extractors:

- `TfidfEngineer`: TF-IDF vector (top 1000 features)
- `LengthEngineer`: Ticket length (number of characters)
- `SentimentEngineer`: Sentiment polarity using TextBlob

All combined through `FeatureCombiner`:

### 3. Multi-Task Classification

Two models were trained:

- `issue_type_classifier.pkl` → predicts `issue_type`
- `urgency_level_classifier.pkl` → predicts `urgency_level`

Each uses `RandomForestClassifier` from `sklearn` and follows a `Classifier` interface.

Model performance is printed via `classification_report`.

### 4. Entity Extraction

Used rule-based NLP (no LLMs):

- Extracted product names from known list
- Extracted dates via regex
- Extracted complaint keywords via matching

Class used: `RuleBasedEntityExtractor` implementing `EntityExtractor` interface.

### 5. Integration

Built a single class:
TicketProcessor().process(text)
>>>>>>> 4bd05bd (Task1 is complete)
