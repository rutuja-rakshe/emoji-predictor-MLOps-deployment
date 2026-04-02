from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictRequest(BaseModel):
    text: str

# Simple prediction logic (no ML dependency)
def predict_logic(text):
    text = text.lower()
    if "happy" in text or "love" in text:
        return "😊"
    elif "sad" in text or "bad" in text:
        return "😢"
    elif "party" in text or "excited" in text:
        return "🎉"
    elif "angry" in text or "hate" in text:
        return "😡"
    else:
        return "😊"

@app.get("/")
def home():
    return {"message": "Emoji Predictor API Running 🚀"}

@app.post("/predict")
def predict(request: PredictRequest):
    return {"emoji": predict_logic(request.text)}