from fastapi import FastAPI
from routes.prediction import router as prediction_router

app = FastAPI(
    title="AgroCulture AI API",
    description="AI Crop Recommendation Backend",
    version="1.0"
)

@app.get("/")
def root():
    return {"message": "AgroCulture AI Backend Running"}

# include prediction routes
app.include_router(prediction_router, prefix="/api")