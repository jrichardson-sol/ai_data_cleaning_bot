import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully! Shape: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Summarize the dataset
def summarize_data(df):
    print("\nDataset Summary:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDuplicate Rows:", df.duplicated().sum())

# Handle missing values using KNN Imputer
def handle_missing_values(df):
    print("Handling missing values using KNN Imputer...")
    
    # Select only numerical columns
    numerical_columns = df.select_dtypes(include=[np.number]).columns
    
    # Impute missing values only for numerical columns
    if len(numerical_columns) > 0:
        imputer = KNNImputer(n_neighbors=5)
        df[numerical_columns] = imputer.fit_transform(df[numerical_columns])
        print("Missing values handled for numerical columns.")
    else:
        print("No numerical columns available for KNN Imputer.")
    
    return df


# Detect and remove duplicates
def remove_duplicates(df):
    print("Removing duplicate rows...")
    df = df.drop_duplicates()
    print(f"Duplicates removed. New shape: {df.shape}")
    return df

# Detect anomalies using Isolation Forest
def detect_anomalies(df):
    print("Detecting anomalies using Isolation Forest...")
    
    # Select only numerical columns
    numerical_columns = df.select_dtypes(include=[np.number])
    
    if not numerical_columns.empty:
        clf = IsolationForest(contamination=0.1, random_state=42)
        
        # Fit Isolation Forest on numerical data and predict anomalies
        df['anomaly'] = clf.fit_predict(numerical_columns)
        
        # Separate anomalies
        anomalies = df[df['anomaly'] == -1]
        print(f"Anomalies detected: {len(anomalies)}")
    else:
        print("No numerical columns available for anomaly detection.")
        df['anomaly'] = 1  # No anomalies by default
        anomalies = pd.DataFrame()  # Empty DataFrame for anomalies

    return df, anomalies


# Normalize numerical columns
def normalize_data(df):
    print("Normalizing numerical data...")
    scaler = StandardScaler()
    numerical_data = df.select_dtypes(include=[np.number])
    df[numerical_data.columns] = scaler.fit_transform(numerical_data)
    print("Normalization complete.")
    return df

# Save cleaned dataset
def save_cleaned_data(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"Cleaned dataset saved to {output_path}")
    except Exception as e:
        print(f"Error saving dataset: {e}")

# Main function
def main():
    file_path = "data/Austin_Pool_Schedule_20250111.csv"  # Update with your file path
    output_path = "outputs/cleaned_dataset.csv"

    df = load_dataset(file_path)
    if df is not None:
        summarize_data(df)
        df = handle_missing_values(df)
        df = remove_duplicates(df)
        df, anomalies = detect_anomalies(df)
        df = normalize_data(df)
        save_cleaned_data(df, output_path)

if __name__ == "__main__":
    main()
