import numpy as np
from app.model_loader import load_model

def predict_crop(data):

    model = load_model()

    features = np.array([[
        data.nitrogen,
        data.phosphorus,
        data.potassium,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall
    ]])

    prediction = model.predict(features)

    return prediction[0]