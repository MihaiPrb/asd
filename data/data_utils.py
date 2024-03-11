import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize_data(data):
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)
    return pd.DataFrame(normalized_data, columns=data.columns)

def handle_missing_values(data):
    # Fill missing values with appropriate strategy (e.g., mean, median, mode)
    data.fillna(data.mean(), inplace=True)

    # Perform additional missing value handling as needed
    # ...

    return data