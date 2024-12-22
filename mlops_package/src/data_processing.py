import pandas as pd

def load_iris_data(data_path):
    return pd.read_csv(data_path)