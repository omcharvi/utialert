
import joblib
import pandas as pd

# Load the saved ML model
model = joblib.load("ml/model.pkl")

def predict_uti(data):
    # Convert input data into a format the model understands
    input_df = pd.DataFrame([{
        "age": data.age,
        "burning": data.burning,
        "frequent_urge": data.frequent_urge,
        "cloudy_urine": data.cloudy_urine,
        "pelvic_pain": data.pelvic_pain,
        "fever": data.fever,
        "blood_in_urine": data.blood_in_urine,
        "back_pain": data.back_pain,
        "hydration": data.hydration,
        "history": data.history
    }])

    # Get probability of UTI (0 to 1)
    probability = model.predict_proba(input_df)[0][1]

    # Decide risk level
    if probability > 0.7:
        risk_level = "High Risk"
        recommendation = "⚠️ Please consult a doctor immediately!"
    elif probability > 0.4:
        risk_level = "Moderate Risk"
        recommendation = "⚠️ Monitor your symptoms. Consider seeing a doctor."
    else:
        risk_level = "Low Risk"
        recommendation = "✅ Stay hydrated and monitor your symptoms."

    return {
        "probability": round(probability * 100, 2),
        "risk_level": risk_level,
        "recommendation": recommendation
    }