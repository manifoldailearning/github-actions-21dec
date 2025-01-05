import pathlib
import os 
import mlops_package
# Path to the root directory of the project
ROOT_DIR = pathlib.Path(mlops_package.__file__).resolve().parent

DATA_DIR = os.path.join(ROOT_DIR, 'data','raw')
file_name = "iris.csv"

file_path = os.path.join(DATA_DIR, file_name)

MODEL_NAME = "iris_model.joblib"
SAVE_MODEL_DIR = os.path.join(ROOT_DIR, 'model')