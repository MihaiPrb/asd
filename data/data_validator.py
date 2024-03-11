import pandas as pd

def validate_data(data):
    # Check for missing values
    if data.isnull().values.any():
        raise Exception("Data contains missing values.")

    # Check for duplicate records
    if data.duplicated().any():
        raise Exception("Data contains duplicate records.")

    # Perform additional validation checks as needed
    # ...

    return data