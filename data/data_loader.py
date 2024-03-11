import pandas as pd
from data.data_validator import validate_data
from data.data_preprocessor import preprocess_data

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        validated_data = validate_data(data)
        preprocessed_data = preprocess_data(validated_data)
        return preprocessed_data
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error occurred while loading data: {str(e)}")