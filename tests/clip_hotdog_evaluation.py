#OPEN AI
import sys
sys.path.append("/Users/jessica.cebrian/PycharmProjects/hotdot_or_not/")
from sklearn.metrics import confusion_matrix
import torch
from PIL import Image
import os
from sklearn.metrics import confusion_matrix,accuracy_score, precision_score, recall_score, f1_score
import numpy as np
from ms import model,processor

print("loaded model")
print("reading image")



def list_folders(directory):
    # Get list of all items (files and folders) in the directory
    all_items = os.listdir(directory)
    
    # Filter out only the folder names
    folder_names = [item for item in all_items if os.path.isdir(os.path.join(directory, item))]
    
    return folder_names

# Define the folder containing the images
image_classes= list_folders("/Users/jessica.cebrian/PycharmProjects/hotdot_or_not/tests/images/")
print(image_classes)
images = []
true_class_labels =[]
for image_class in image_classes:
  folder_path = f"/Users/jessica.cebrian/PycharmProjects/hotdot_or_not/tests/images/{image_class}"
  
  if image_class != 'hotdog':
    iclass = 'anything_else'
  else: 
    iclass = 'hotdog'   
# Get a list of all files in the folder
  files = os.listdir(folder_path)
  image_files = [file for file in files if file.endswith((".jpeg", ".jpg", ".png"))]
  for file in image_files:
      file_path = os.path.join(folder_path, file)
      try:
        image = Image.open(file_path)
        images.append(image)
        true_class_labels.append(iclass)
      except:
        # print(f"can't process image {file_path}")
        pass

# Inputs to CLIP model
inputs = processor(text=["a photo of a hotdog", "photo of legs","a photo of something else"], images=images, return_tensors="pt", padding=True)

print(f"predicting {len(images)} images")
# Get Outputs from CLIP model
outputs = model(**inputs)
logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities

max_indices = torch.argmax(probs, dim=1)
max_probabilities = torch.max(probs, dim=1).values

class_labels = ["hotdog", "anything_else", "anything_else"]

# Map indices to class labels
max_classes = [class_labels[idx] for idx in max_indices]

class_probability_tuples = [(class_label, np.round(probability.item(),3)) for class_label, probability in zip(max_classes, max_probabilities)]

# print(max_classes)
# print(true_class_labels)

# Calculate confusion matrix
conf_matrix = confusion_matrix(true_class_labels, max_classes, labels=["hotdog", "anything_else"])

# Extract TP, TN, FP, FN
TP = conf_matrix[1, 1]  # True Positives
TN = conf_matrix[0, 0]  # True Negatives
FP = conf_matrix[0, 1]  # False Positives
FN = conf_matrix[1, 0]  # False Negatives

# Print TP, TN, FP, FN
print("True Positives (TP):", TP)
print("True Negatives (TN):", TN)
print("False Positives (FP):", FP)
print("False Negatives (FN):", FN)

# Convert true_set to numpy array for easier comparison
true_labels = np.array(true_class_labels)

# Calculate accuracy
accuracy = accuracy_score(true_class_labels, max_classes)

# Calculate precision, recall, and F1-score for each class
precision = precision_score(true_labels, max_classes, average=None, labels=["hotdog", "anything_else"])
recall = recall_score(true_labels, max_classes, average=None, labels=["hotdog", "anything_else"])
f1 = f1_score(true_labels, max_classes, average=None, labels=["hotdog", "anything_else"])

# Print the performance metrics
print("Accuracy:", accuracy)
print("Precision (Hotdog):", precision[0])
print("Precision (Anything Else):", precision[1])
print("Recall (Hotdog):", recall[0])
print("Recall (Anything Else):", recall[1])
print("F1-score (Hotdog):", f1[0])
print("F1-score (Anything Else):", f1[1])