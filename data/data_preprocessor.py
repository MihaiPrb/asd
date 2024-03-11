import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

def preprocess_data(data):
    # Handle missing values
    data.fillna(method='ffill', inplace=True)
    data.fillna(method='bfill', inplace=True)

    # Convert categorical variables to numerical using label encoding
    categorical_columns = data.select_dtypes(include=['object']).columns
    label_encoder = LabelEncoder()
    for column in categorical_columns:
        data[column] = label_encoder.fit_transform(data[column])

    # Scale numerical features using Min-Max scaling
    numerical_columns = data.select_dtypes(include=['float', 'int']).columns
    scaler = MinMaxScaler()
    data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

    return data

def split_data(data, train_ratio=0.8):
    train_size = int(len(data) * train_ratio)
    train_data = data[:train_size]
    test_data = data[train_size:]
    return train_data, test_data

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    preprocessed_data = preprocess_data(data)
    return preprocessed_data

def feature_engineering(data):
    # Perform feature engineering tasks specific to your data and problem
    # Example: Create new features, drop irrelevant columns, etc.
    # You can customize this function based on your requirements
    return data