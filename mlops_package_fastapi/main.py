# Build fastapi application
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib
import pandas as pd
import os
import pathlib
import sys

# read the model from model directory
model_dir = pathlib.Path(__file__).parent / "model"
src = pathlib.Path(__file__).parent / "src"
sys.path.append(str(src))    # Add the src directory to the path
print(model_dir)
model_path = model_dir / "iris_model.joblib"
model = joblib.load(model_path)

app = FastAPI()

@app.get('/')
def home():
    return "Welcome to Fast API Application"

class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post('/predict')
def predict(iris_data: Iris):
    data = iris_data.model_dump()
    sepal_length = data['sepal_length']
    sepal_width = data['sepal_width']
    petal_length = data['petal_length']
    petal_width = data['petal_width']
    data = {
        'sepal.length': sepal_length,
        'sepal.width': sepal_width,
        'petal.length': petal_length,
        'petal.width': petal_width
    }
    features = pd.DataFrame(data, index=[0])

    # make a prediction
    species = model.predict(features)
    return {"species prediction": species[0]}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1",port=8002)