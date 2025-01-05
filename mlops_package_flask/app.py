from flask import Flask,render_template,request
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

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])
    data = {
        'sepal.length': sepal_length,
        'sepal.width': sepal_width,
        'petal.length': petal_length,
        'petal.width': petal_width
    }
    features = pd.DataFrame(data, index=[0])

    # make a prediction
    species = model.predict(features)
    return render_template('index.html', species=species[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=8002)