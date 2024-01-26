import pandas as pd
from ms import hotdog_model


def predict(hotdog_model):
    prediction = hotdog_model.predict()
    return prediction


def get_model_response(input = None):
    if input:
        X = pd.json_normalize(input.__dict__) # uncomment this if input is json from curl
    prediction = predict(hotdog_model)
    if prediction == 1:
        # label = "M"
        label = "Hotdog"
    else:
        # label = "B"
        label = "Not Hotdog"
    return {
        'label': label,
        'prediction': int(prediction)
    }
