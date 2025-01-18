
import logging
import warnings
from urllib.parse import urlparse
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_openml
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

import mlflow
import mlflow.sklearn
from mlflow.models import infer_signature

# Initializing the logger to log information
logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

# Function to calculate the evaluation metrics - rmse, mae and r2
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

def init_LRModel():
    model = LinearRegression()
    return model

def init_RFModel():
    params = {"max_depth": 4, "random_state": 42}
    model = RandomForestRegressor(**params)
    return model, params
        

if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Load the Ames Housing Dataset
    housing = fetch_openml(name="house_prices", as_frame=True)
    X = housing.data[["GrLivArea", "YearBuilt"]] # Select a few features
    # X = housing.data[["GrLivArea", "YearBuilt", "LotArea"]] # Select a few features
    y = housing.target
        # Split the data into training and test sets. (0.8, 0.2) split.
    train_x, test_x, train_y, test_y = train_test_split(X,y, test_size=0.2, random_state=42)

    
    with mlflow.start_run():
        # Regression Model using Simple Linear Regression
        # model = init_LRModel()
        
        # Regression Model using Random Forest Regressor
        model, params = init_RFModel()
        
        model.fit(train_x, train_y)
        predicted_prices = model.predict(test_x)

        (rmse, mae, r2) = eval_metrics(test_y, predicted_prices)

        # print(f"Linear Regression model:")
        print(f"Random Forest model:")
        print(f"  RMSE: {rmse}")
        print(f"  MAE: {mae}")
        print(f"  R2: {r2}")

        # Log metrics using the MLflow APIs
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)

        # Log parameters using the MLflow APIs for Random Forest Model
        mlflow.log_params(params)

        predictions = model.predict(train_x)
        signature = infer_signature(train_x, predictions)

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Log the sklearn model and register the model version
        mlflow.sklearn.log_model(
            sk_model = model, 
            # artifact_path = "linear model", 
            # registered_model_name="LinearRegressionModel", 
            artifact_path = "Random Forest model",
            registered_model_name="RandomForestModel",
            signature=signature)