# Imports
from fastapi import FastAPI
import joblib
import traceback
import pickle
import gzip
from ms.hotdog_model import HotdogModel

# Initialize FastAPI app
app = FastAPI()

# Load model
# model = joblib.load('model/model_binary.dat.gz')

hotdog_model = HotdogModel()  

# TODO: be able to import model from picked file. currenty failing.
# # Load Hotdog model
# try:
#     with gzip.open('model/hotdog_model.pkl.gz', 'rb') as f:
#         hotdog_model = pickle.load(f)
# except Exception as e:
#     print(f"Error loading model: {e}")
#     print(traceback.format_exc()) 