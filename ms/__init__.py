# Imports
from fastapi import FastAPI
from ms.hotdog_model import HotdogModel
from transformers import CLIPProcessor, CLIPModel

# Initialize FastAPI app
app = FastAPI()

# Load model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

