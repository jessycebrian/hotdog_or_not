import streamlit as st
import requests
from PIL import Image
import io
from ms import processor,model
from ms.functions import predict_label_and_probabilities
from fastapi import FastAPI, File, UploadFile


# Function to make a prediction request to the FastAPI service
def predict(image_bytes):
    # Wrap the byte data into a file-like object
    image_file = io.BytesIO(image_bytes)
    
    files = {'file': image_file}
    response = requests.post('http://localhost:8000/predict', files=files)
    if response.status_code == 200:
        result = response.json()
        return result
    else:
        return {'label': 'Error', 'prediction': 'Error'}

# Function to make a prediction request to the FastAPI service
def predict_clip(image_bytes):
    # Wrap the byte data into a file-like object
    image_file = io.BytesIO(image_bytes)
    contents = image_file.read()
    image = Image.open(io.BytesIO(contents))
    inputs = processor(text=["a photo of a hotdog", "photo of legs", "a photo of something else"], images=image, return_tensors="pt", padding=True)

    outputs = model(**inputs)
    result = predict_label_and_probabilities(outputs)
    return result
    
    

# Streamlit app
def main():
    st.title("Hotdog Or Not: Hotdog Recognition App")

    # File upload widget
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image file as bytes
        image_bytes = uploaded_file.read()
        # Display the image
        st.image(image_bytes, caption="Uploaded Image", use_column_width=True)

        # Check if user clicks the predict button
        if st.button('Predict'):
            # Make prediction request
            result = predict_clip(image_bytes)
            # Display prediction result
            st.write("Label:", result['label'])
            st.write("Prediction:", result['prediction'])

if __name__ == '__main__':
    main()
