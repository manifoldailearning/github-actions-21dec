# Streamlit application for the Machine Learning Model

import streamlit as st
import joblib
import pandas as pd
import os
import pathlib

# get the input from the user


sepal_length = st.sidebar.slider("Sepal Length", 4.3, 7.9, 5.4)
sepal_width = st.sidebar.slider("Sepal Width", 2.0, 4.4, 3.4)
petal_length = st.sidebar.slider("Petal Length", 1.0, 6.9, 1.3)
petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 0.2)
data = {
    'sepal.length': sepal_length,
    'sepal.width': sepal_width,
    'petal.length': petal_length,
    'petal.width': petal_width
}
features = pd.DataFrame(data, index=[0])

# read the model from model directory
model_dir = pathlib.Path(__file__).parent / "model"
model_path = model_dir / "iris_model.joblib"
model = joblib.load(model_path)


# make a prediction
species = model.predict(features)
# display the result
st.title("Iris Flower Species Prediction")
st.write("The input features are:")
st.write(features)

st.write(f"The species of iris flower is: {species[0]}")
