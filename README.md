
# 🏥 UTIAlert – Early UTI Detection Assistant

A healthcare web application that helps women, especially in rural areas, 
detect early signs of Urinary Tract Infections (UTIs) at home.

---

## 🎯 Features

- ✅ Symptom-based UTI risk prediction using Machine Learning
- ✅ Color-coded risk results (High / Moderate / Low)
- ✅ Actionable recommendations based on risk level
- ✅ Educational content about UTIs
- ✅ Simple, mobile-friendly interface
- ✅ Fast API backend with FastAPI
- ✅ Privacy-first — no personal data stored

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit (Python) |
| Backend API | FastAPI (Python) |
| Machine Learning | scikit-learn (Random Forest) |
| Data | Synthetic UTI Dataset (500 records) |
| Storage | None (privacy-first) |

---

## 📁 Project Structure
```
utialert/
├── app.py                  # Streamlit frontend
├── backend/
│   ├── main.py             # FastAPI app
│   ├── model.py            # ML model loader
│   ├── schemas.py          # Data models
│   └── __init__.py
├── ml/
│   ├── train_model.py      # Model training script
│   └── model.pkl           # Saved trained model
├── data/
│   ├── create_data.py      # Dataset generator
│   └── uti_data.csv        # Training dataset
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Clone & Setup
```bash
git clone <your-repo-url>
cd utialert
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Train the Model
```bash
python data/create_data.py
python ml/train_model.py
```

### 3. Start the Backend
```bash
uvicorn backend.main:app --reload
```

### 4. Start the Frontend (new terminal)
```bash
streamlit run app.py
```

### 5. Open in Browser
```
http://localhost:8501
```

---

## 📊 ML Model Performance

| Metric | Score |
|---|---|
| Algorithm | Random Forest Classifier |
| Training Samples | 400 |
| Testing Samples | 100 |
| Target Accuracy | ≥ 80% |

---

## ⚠️ Disclaimer

This tool is **not a substitute** for professional medical advice.
Always consult a qualified healthcare professional for diagnosis and treatment.

---

## 👩‍💻 Developed By

- **Your Name**
- Internship Project — 2026
- Built with Python, Streamlit, FastAPI & scikit-learn