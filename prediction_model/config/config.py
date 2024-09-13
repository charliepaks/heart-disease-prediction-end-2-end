import pathlib
import os
import prediction_model

PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT,"datasets")

FILE_NAME = 'heart_disease_classification_dataset.csv'
TEST_FILE = "test_data.csv"

MODEL_NAME = 'classification.pkl'
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,'trained_models')

TARGET = 'target'

#Final features used in the model
FEATURES = ['age', 'sex', 'cp', 'trestbps',
       'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope','ca', 'thal', 'target']

PRED_FEATURES = ['age', 'sex', 'cp', 'trestbps',
       'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope','ca', 'thal']

NUM_FEATURES = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

CAT_FEATURES = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal', 'target']