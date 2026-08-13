import pickle
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Load trained LogisticRegression model and TfidfVectorizer
with open('spam_ham_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

app = FastAPI(
    title="Email Spam/Ham Classifier API",
    description="Machine Learning API predicting if an email or message is Spam or Legitimate (Ham)"
)

# Enable CORS for local browser access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailInput(BaseModel):
    text: str = Field(..., example="WINNER!! As a valued network customer you have been selected to receive a £900 prize reward!")

class PredictionResponse(BaseModel):
    label: str
    is_spam: bool
    confidence: float
    spam_probability: float
    ham_probability: float

@app.get("/")
def home():
    return {"message": "Email Spam/Ham Classifier API is live!"}

@app.post("/predict", response_model=PredictionResponse)
@app.post("/predict/spam", response_model=PredictionResponse)
def predict_spam(data: EmailInput):
    # Vectorize input text using trained TF-IDF
    features = vectorizer.transform([data.text])
    
    # Predict class (0 = spam, 1 = ham)
    pred = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]
    
    spam_prob = float(probabilities[0])
    ham_prob = float(probabilities[1])
    is_spam_bool = bool(pred == 0)
    
    return PredictionResponse(
        label="Spam" if is_spam_bool else "Ham",
        is_spam=is_spam_bool,
        confidence=round(spam_prob if is_spam_bool else ham_prob, 4),
        spam_probability=round(spam_prob, 4),
        ham_probability=round(ham_prob, 4)
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
