import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dataset Loaded Successfully!\n")
        print(df.head())
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Step 2: Check Dataset Structure
def check_structure(df):
    print("\n--- Dataset Info ---\n")
    print(df.info())
    print("\n--- Missing Values ---\n")
    print(df.isnull().sum())
    print("\n--- Statistical Summary ---\n")
    print(df.describe())

# Step 3: Target Variable Analysis
def analyze_target(df, target_column):
    print("\n--- Target Variable Analysis ---\n")
    print(df[target_column].value_counts())
    sns.countplot(x=target_column, data=df)
    plt.title("Target Variable Distribution")
    plt.show()

# Step 4: Correlation and Relationships
def analyze_relationships(df, target_column):
    print("\n--- Correlation Matrix ---\n")
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Feature Correlation")
    plt.show()

    # Pairplot for visualizing relationships
    sns.pairplot(df, hue=target_column)
    plt.show()

# Run the EDA
def main():
    file_path = "ai4i2020.csv"  # Update with your file path
    target_column = "Machine failure"  # Update based on your dataset

    df = load_data(file_path)
    if df is not None:
        check_structure(df)
        analyze_target(df, target_column)
        analyze_relationships(df, target_column)

if __name__ == "__main__":
    main()
