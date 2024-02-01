#OPEN AI


from PIL import Image
import requests

from transformers import CLIPProcessor, CLIPModel

model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
print("loaded model")
print("reading image")

file_path = "hotdog_or_leg.jpeg"
image = Image.open(file_path)

inputs = processor(text=["a photo of a hotdog", "photo of legs","a photo of something else"], images=image, return_tensors="pt", padding=True)

print("predicting")

outputs = model(**inputs)
logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities
if float(probs[0][0]) > 0.6:
  output=f"The image is a hotdog with probability: {float(probs[0][0])}"
else:
  output= "The image is not a hotdog"

print(probs)
print(output)