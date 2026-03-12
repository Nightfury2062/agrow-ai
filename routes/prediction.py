from fastapi import APIRouter
from app.schemas import CropInput
from app.predictor import predict_crop
from app.utils import soil_recommendation

router = APIRouter()


@router.post("/predict")
def predict(data: CropInput):

    crop = predict_crop(data)

    soil_advice = soil_recommendation(
        data.nitrogen,
        data.phosphorus,
        data.potassium
    )

    return {
        "recommended_crop": crop,
        "soil_suggestions": soil_advice
    }