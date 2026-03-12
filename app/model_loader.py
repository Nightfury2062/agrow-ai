import joblib
import os

MODEL_PATH = os.path.join("model", "crop_model.pkl")
SCALER_PATH = os.path.join("model", "scaler.pkl")
ENCODER_PATH = os.path.join("model", "label_encoder.pkl")

model = None
scaler = None
encoder = None


def load_components():
    global model, scaler, encoder

    if model is None:
        model = joblib.load(MODEL_PATH)

    if scaler is None:
        scaler = joblib.load(SCALER_PATH)

    if encoder is None:
        encoder = joblib.load(ENCODER_PATH)

    return model, scaler, encoder