import pandas as pd

def analyze_csv(file_path):
    # Read CSV file
    df = pd.read_csv(file_path)

    # Display basic information
    print("Basic Information:")
    print(df.info())
    print("\n")

    # Display first few rows
    print("First 5 Rows:")
    print(df.head())
    print("\n")

    # Summary statistics (only numerical columns)
    print("Summary Statistics:")
    print(df.describe())  # This will work correctly as it excludes non-numeric data
    print("\n")

    # Check for missing values
    print("Missing Values:")
    print(df.isnull().sum())
    print("\n")

    # Display unique values count for categorical columns
    categorical_columns = df.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        print(f"Unique values in {col}:")
        print(df[col].value_counts())
        print("\n")

    # Correlation matrix for numerical columns only
    print("Numerical Data Only:")
    numeric_df = df.select_dtypes(include=['number'])  # Select only numeric columns
    print(numeric_df.corr())
    print("\n")

# Example usage
if __name__ == "__main__":
    file_path = "sample_data.csv"  # Ensure the correct CSV file path
    analyze_csv(file_path)
