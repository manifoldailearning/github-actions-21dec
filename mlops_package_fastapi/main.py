# Import necessary libraries and modules
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib
import pandas as pd
import os
import pathlib
import sys

# Define the directory where the model is stored
model_dir = pathlib.Path(__file__).parent / "model"
# Define the source directory and add it to the system path
src = pathlib.Path(__file__).parent / "src"
sys.path.append(str(src))    # Add the src directory to the path
print(model_dir)

# Define the path to the model file and load the model
model_path = model_dir / "iris_model.joblib"
model = joblib.load(model_path)

# Create a FastAPI application instance
app = FastAPI()

# Define a root endpoint that returns a welcome message
@app.get('/')
def home():
    return "Welcome to Fast API Application"

# Define a Pydantic model for the input data
class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Define an endpoint for making predictions
@app.post('/predict')
def predict(iris_data: Iris):
    # Convert the input data to a dictionary
    data = iris_data.model_dump()
    sepal_length = data['sepal_length']
    sepal_width = data['sepal_width']
    petal_length = data['petal_length']
    petal_width = data['petal_width']
    
    # Create a DataFrame from the input data
    data = {
        'sepal.length': sepal_length,
        'sepal.width': sepal_width,
        'petal.length': petal_length,
        'petal.width': petal_width
    }
    features = pd.DataFrame(data, index=[0])

    # Make a prediction using the loaded model
    species = model.predict(features)
    
    # Return the prediction result
    return {"species prediction": species[0]}

# Run the FastAPI application using Uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8002)