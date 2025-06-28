from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from clean_and_prepare import clean_text
import uvicorn

# Load model and vectorizer once
model = joblib.load("logreg_sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Label map
label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}

# FastAPI app
app = FastAPI(title="Myntra Review Sentiment API")

# Request body schema
class ReviewRequest(BaseModel):
    review: str

# Root endpoint
@app.get("/")
def home():
    return {"message": "Myntra Sentiment Classifier is running"}

# Predict endpoint
@app.post("/predict")
def predict_sentiment(data: ReviewRequest):
    review = data.review.strip()
    if not review:
        return {"error": "Review text is empty."}

    cleaned = clean_text(review)
    X_input = vectorizer.transform([cleaned])
    pred = model.predict(X_input)[0]
    prob = model.predict_proba(X_input).max()

    return {
        "review": review,
        "cleaned_review": cleaned,
        "predicted_sentiment": label_map[pred],
        "confidence": round(float(prob), 4)
    }

