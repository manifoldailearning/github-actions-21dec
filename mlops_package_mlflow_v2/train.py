#!/usr/bin/env python
import pandas as pd
from pathlib import Path
import os 
import sys 
import joblib
import mlflow
import mlflow.sklearn

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from src.model import IrisClassifier
from src.data_processing import load_iris_data
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
import config

def main():
    # set tracking URL
    mlflow.set_tracking_uri("http://localhost:5001")

    # mlflow.set_experiment("Iris_Classification_1")

    with mlflow.start_run(run_name="Iris_Classification_1"):
        
        
        # log params

        mlflow.log_param("model_name", "Logistic Regression")
        mlflow.log_param("random_state", 42)
        mlflow.log_param("test_size", 0.2)

        data_path = config.file_path 

        df = load_iris_data(data_path)

        X = df.drop('species', axis=1)
        y = df['species']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = IrisClassifier()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy:", accuracy)
        mlflow.log_metric("accuracy", accuracy)

        # Save the model
        mlflow.sklearn.log_model(model, artifact_path="model")
        joblib.dump(model,os.path.join(config.SAVE_MODEL_DIR, config.MODEL_NAME))

if __name__ == '__main__':
    main()