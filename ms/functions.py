from torch import Tensor



def predict_label_and_probabilities(outputs: Tensor, threshold: float = 0.6):
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)

    label = "hotdog" if float(probs[0][0]) > threshold else "not a hotdog"
    prediction = float(probs[0][0]) if label == "hotdog" else float(probs[0][1])

    return {"label": label, "prediction": prediction}
