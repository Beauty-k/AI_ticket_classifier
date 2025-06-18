import pandas as pd

def load_data():
    df = pd.read_excel("data/ai_dev_assignment_tickets_complex_1000.xls")
    print(df.head())
    return df

if __name__ == "__main__":
    df = load_data()
    print("Columns:", df.columns.tolist())
    print("\nMissing values:\n", df.isnull().sum())
    print("\nUnique issue types:", df['issue_type'].unique())
    print("Unique urgency levels:", df['urgency_level'].unique())
    print("\nSample ticket text:\n", df['ticket_text'].iloc[0])