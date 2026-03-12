from fastapi import FastAPI
from backend.schemas import UserInputSchema, PredictionResult
from backend.model import predict_uti

# Create FastAPI app
app = FastAPI(title="UTIAlert API", version="1.0")

# Home route - just to test if API is running
@app.get("/")
def home():
    return {"message": "UTIAlert API is running! ✅"}

# Predict route - receives symptoms, returns prediction
@app.post("/predict")
def predict(data: UserInputSchema):
    result = predict_uti(data)
    return result

# Education route - returns UTI info
@app.get("/education")
def education():
    return {
        "what_is_uti": "A UTI is an infection in the urinary system caused by bacteria.",
        "common_symptoms": [
            "Burning sensation while urinating",
            "Frequent urge to urinate",
            "Cloudy or strong-smelling urine",
            "Pelvic pain",
            "Fever or chills"
        ],
        "prevention_tips": [
            "Drink plenty of water daily",
            "Urinate after sexual activity",
            "Wipe front to back",
            "Avoid holding urine for long",
            "Wear breathable cotton underwear"
        ],
        "when_to_see_doctor": "If symptoms persist more than 2 days or you have fever and back pain, see a doctor immediately."
    }
