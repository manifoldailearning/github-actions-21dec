import pytest
import pandas as pd
from sklearn.datasets import load_iris
import sys
import pathlib
import os 
from pathlib import Path
import joblib

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))
file_path = "model/iris_model.joblib"
saved_path = os.path.join(PACKAGE_ROOT,file_path)

from src.data_processing import load_iris_data


@pytest.fixture()
def sample_iris_data():
    data_path = config.file_path 
    df = load_iris_data(data_path)
    X = df.drop('species', axis=1)
    y = df['species']
    return X, y

def test_model_predict(sample_iris_data):
    X, y = sample_iris_data
    model = joblib.load(saved_path)
    predictions = model.predict(X[:5])  # Predict on a few samples
    assert all(predictions == y[:5])  # Simplified accuracy check 