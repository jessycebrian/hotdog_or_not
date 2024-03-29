import streamlit as st
import requests
from PIL import Image
import io

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
            result = predict(image_bytes)
            # Display prediction result
            st.write("Label:", result['label'])
            st.write("Prediction:", result['prediction'])

if __name__ == '__main__':
    main()
