from torch import Tensor
import torch


def predict_label_and_probabilities(outputs: Tensor, threshold: float = 0.6):
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)
    max_index = torch.argmax(probs, dim=1)
    max_prob = torch.max(probs, dim=1).values
    class_labels = ["hotdog", "anything_else", "anything_else"]
    # Map indices to class labels
    max_class = class_labels[max_index]
    if max_class == "hotdog" and max_prob >= 0.6:
        label = max_class
        prediction = max_prob
    elif max_class == "hotdog" and max_prob < 0.6:
        label =  "not a hotdog"
        prediction =  1 - max_prob
    else:
        label = "not a hotdog"
        prediction = max_prob

    return {"label": label, "prediction": prediction}
