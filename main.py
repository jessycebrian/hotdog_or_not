# Local imports
import datetime
from typing import Optional
# Third party imports
from pydantic import BaseModel, Field

from ms import app,model,processor
from ms.functions import predict_label_and_probabilities
from fastapi import FastAPI, File, UploadFile

from PIL import Image
import io

model_name = "Hotdog Recognition Model (CLIP) (2024)"
version = "v2.0.0"


# Input for data validation
# Not used
class Input(BaseModel):
    file: UploadFile

class FileInput(BaseModel):
    file_bytes: bytes


# Output for data validation
class Output(BaseModel):
    label: str
    prediction: float


@app.get('/')
async def model_info():
    """Return model information, version, how to call"""
    return {
        "name": model_name,
        "version": version
    }


@app.get('/health')
async def service_health():
    """Return service health"""
    return {
        "ok"
    }


@app.post('/predict', response_model=Output) # Change to post method when input data
async def model_predict(file: UploadFile = File(...)):
    """Predict with input"""
    """Predict with input image"""
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    inputs = processor(text=["a photo of a hotdog", "a photo of something else"], images=image, return_tensors="pt", padding=True)

    outputs = model(**inputs)
    result = predict_label_and_probabilities(outputs)


    return result


@app.post("/predict_streamlit",response_model=Output)
async def model_predict(file: UploadFile = File(...)):
        # Open the image from bytes
    image = Image.open(io.BytesIO(await file.read()))    

    print("read Image")
    inputs = processor(text=["a photo of a hotdog","photo of legs", "a photo of something else"], images=image, return_tensors="pt", padding=True)

    outputs = model(**inputs)
    result = predict_label_and_probabilities(outputs)
        
    # Return the prediction result
    return result
    