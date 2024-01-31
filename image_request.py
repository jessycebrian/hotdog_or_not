import requests

# URL of the FastAPI endpoint
url = "http://127.0.0.1:8000/predict"

# Path to the image file
file_path = "hotdog_test.jpg"
# file_path = "CLIP.png"

# Open the image file
with open(file_path, "rb") as file:
    # Create a dictionary containing the file object
    files = {"file": file}

    # Send the POST request with the image file
    response = requests.post(url, files=files)

# Print the response from the FastAPI endpoint
print(response.json())
