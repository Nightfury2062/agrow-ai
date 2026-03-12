import numpy as np
from app.model_loader import load_components


def predict_crop(data):

    model, scaler, encoder = load_components()

    features = np.array([[
        data.nitrogen,
        data.phosphorus,
        data.potassium,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall
    ]])

    # scale input
    scaled_features = scaler.transform(features)

    # predict
    prediction = model.predict(scaled_features)

    # decode label
    crop = encoder.inverse_transform(prediction)

    return crop[0]