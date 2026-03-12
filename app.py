import streamlit as st
import pandas as pd
import joblib
import os

# ── Page Configuration ────────────────────────────────
st.set_page_config(
    page_title="UTIAlert – Early UTI Detection",
    page_icon="🏥",
    layout="centered"
)

# ── Backend API URL ───────────────────────────────────
API_URL = "https://utialert-backend.onrender.com"

# ── Load ML Model directly ────────────────────────────
@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "ml", "model.pkl")
    return joblib.load(model_path)

model = load_model()

# ── Prediction Function ───────────────────────────────
def predict_uti(age, burning, frequent_urge, cloudy_urine,
                pelvic_pain, fever, blood_in_urine, back_pain,
                hydration, history):

    input_df = pd.DataFrame([{
        "age": age,
        "burning": burning,
        "frequent_urge": frequent_urge,
        "cloudy_urine": cloudy_urine,
        "pelvic_pain": pelvic_pain,
        "fever": fever,
        "blood_in_urine": blood_in_urine,
        "back_pain": back_pain,
        "hydration": hydration,
        "history": history
    }])

    probability = model.predict_proba(input_df)[0][1]

    if probability > 0.7:
        risk_level = "High Risk"
        recommendation = "⚠️ Please consult a doctor immediately!"
    elif probability > 0.4:
        risk_level = "Moderate Risk"
        recommendation = "⚠️ Monitor your symptoms. Consider seeing a doctor."
    else:
        risk_level = "Low Risk"
        recommendation = "✅ Stay hydrated and monitor your symptoms."

    return round(probability * 100, 2), risk_level, recommendation

# ── Custom Styling ────────────────────────────────────
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #d63384;
        text-align: center;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #6c757d;
        text-align: center;
        margin-bottom: 2rem;
    }
    .risk-high {
        background-color: #ffe0e0;
        border-left: 6px solid #dc3545;
        padding: 1rem;
        border-radius: 8px;
        font-size: 1.2rem;
        font-weight: bold;
        color: #dc3545;
    }
    .risk-moderate {
        background-color: #fff8e0;
        border-left: 6px solid #ffc107;
        padding: 1rem;
        border-radius: 8px;
        font-size: 1.2rem;
        font-weight: bold;
        color: #856404;
    }
    .risk-low {
        background-color: #e0f8e9;
        border-left: 6px solid #28a745;
        padding: 1rem;
        border-radius: 8px;
        font-size: 1.2rem;
        font-weight: bold;
        color: #28a745;
    }
    .section-header {
        font-size: 1.4rem;
        font-weight: 700;
        color: #d63384;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .disclaimer {
        background-color: #fff3cd;
        border: 1px solid #ffc107;
        padding: 0.8rem;
        border-radius: 8px;
        font-size: 0.85rem;
        color: #856404;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────
st.markdown('<div class="title">🏥 UTIAlert</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Early UTI Detection Assistant for Women</div>', unsafe_allow_html=True)
st.markdown('<div class="disclaimer">⚠️ This tool is <b>not a substitute</b> for professional medical advice. Always consult a doctor.</div>', unsafe_allow_html=True)
st.markdown("---")

# ── Sidebar ───────────────────────────────────────────
with st.sidebar:
    st.image("https://img.icons8.com/color/96/hospital.png", width=80)
    st.markdown("## 🏥 UTIAlert")
    st.markdown("**Early UTI Detection Assistant**")
    st.markdown("---")
    st.markdown("### 📌 How to Use")
    st.markdown("""
    1. Enter your **age** and **water intake**
    2. Select your **symptoms**
    3. Click **Analyze My Symptoms**
    4. Get your **risk result** instantly!
    """)
    st.markdown("---")
    st.markdown("### 📊 Risk Levels")
    st.markdown("🔴 **High Risk** — See doctor now")
    st.markdown("🟡 **Moderate Risk** — Monitor closely")
    st.markdown("🟢 **Low Risk** — Stay hydrated")
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.markdown("Built with ❤️ using Python, Streamlit & scikit-learn")
    st.markdown("---")
    st.markdown('<p style="font-size:0.75rem;color:gray;">⚠️ Not a substitute for medical advice</p>', unsafe_allow_html=True)

# ── Navigation Tabs ───────────────────────────────────
tab1, tab2 = st.tabs(["🩺 Check My Risk", "📚 Learn About UTI"])

# ════════════════════════════════════════════════════
# TAB 1 — SYMPTOM CHECKER
# ════════════════════════════════════════════════════
with tab1:
    st.markdown('<div class="section-header">Step 1: Your Basic Information</div>', unsafe_allow_html=True)

    age = st.slider("Your Age", min_value=10, max_value=80, value=25, step=1)

    hydration_option = st.radio(
        "How much water do you drink daily?",
        ["Low (less than 4 glasses)", "Moderate (4–8 glasses)", "High (more than 8 glasses)"],
        horizontal=True
    )
    hydration = 0 if "Low" in hydration_option else (1 if "Moderate" in hydration_option else 2)

    history = 1 if st.radio(
        "Have you had a UTI before?",
        ["No", "Yes"],
        horizontal=True
    ) == "Yes" else 0

    st.markdown('<div class="section-header">Step 2: Select Your Symptoms</div>', unsafe_allow_html=True)
    st.write("Check all symptoms you are currently experiencing:")

    col1, col2 = st.columns(2)

    with col1:
        burning = 1 if st.checkbox("🔥 Burning sensation while urinating") else 0
        frequent_urge = 1 if st.checkbox("🚽 Frequent urge to urinate") else 0
        cloudy_urine = 1 if st.checkbox("💧 Cloudy or strong-smelling urine") else 0
        pelvic_pain = 1 if st.checkbox("😣 Pelvic pain or pressure") else 0

    with col2:
        fever = 1 if st.checkbox("🌡️ Fever or chills") else 0
        blood_in_urine = 1 if st.checkbox("🩸 Blood in urine") else 0
        back_pain = 1 if st.checkbox("🔙 Lower back or side pain") else 0

    st.markdown("---")

    if st.button("🔍 Analyze My Symptoms", use_container_width=True):
        with st.spinner("Analyzing your symptoms..."):
            probability, risk_level, recommendation = predict_uti(
                age, burning, frequent_urge, cloudy_urine,
                pelvic_pain, fever, blood_in_urine, back_pain,
                hydration, history
            )

        st.markdown("## 📊 Your Results")
        st.markdown(f"**UTI Risk Probability: {probability}%**")
        st.progress(int(probability))

        if "High" in risk_level:
            st.markdown(f'<div class="risk-high">🔴 {risk_level}</div>', unsafe_allow_html=True)
        elif "Moderate" in risk_level:
            st.markdown(f'<div class="risk-moderate">🟡 {risk_level}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="risk-low">🟢 {risk_level}</div>', unsafe_allow_html=True)

        st.markdown("### 💊 Recommendation")
        st.info(recommendation)

        if "High" in risk_level:
            st.error("Please do not ignore these symptoms. Visit a doctor as soon as possible.")
            st.markdown("**Next steps:**")
            st.markdown("- 🏥 Visit your nearest clinic or hospital")
            st.markdown("- 💊 A simple antibiotic course can treat UTI quickly")
            st.markdown("- 💧 Drink plenty of water in the meantime")
        elif "Moderate" in risk_level:
            st.warning("Keep monitoring. If symptoms worsen in 24 hours, see a doctor.")
            st.markdown("- 💧 Drink at least 8 glasses of water today")
            st.markdown("- 🚫 Avoid caffeine and alcohol")
            st.markdown("- 🌡️ Monitor your temperature")
        else:
            st.success("You seem okay! Stay hydrated and maintain good hygiene.")
            st.markdown("- 💧 Keep drinking water regularly")
            st.markdown("- 🧼 Maintain good personal hygiene")
            st.markdown("- 📅 Check again if new symptoms appear")

# ════════════════════════════════════════════════════
# TAB 2 — EDUCATION
# ════════════════════════════════════════════════════
with tab2:
    st.markdown('<div class="section-header">📖 What is a UTI?</div>', unsafe_allow_html=True)
    st.write("A **Urinary Tract Infection (UTI)** is a bacterial infection that affects the urinary system — including the bladder, urethra, and kidneys. It is one of the most common infections in women.")

    st.markdown('<div class="section-header">⚠️ Common Symptoms</div>', unsafe_allow_html=True)
    for s in ["🔥 Burning sensation while urinating", "🚽 Frequent urge to urinate",
              "💧 Cloudy, dark, or strong-smelling urine", "😣 Pelvic pain or pressure",
              "🌡️ Fever or chills", "🩸 Blood in urine", "🔙 Lower back or side pain"]:
        st.markdown(f"- {s}")

    st.markdown('<div class="section-header">🛡️ Prevention Tips</div>', unsafe_allow_html=True)
    for t in ["💧 Drink 8–10 glasses of water daily", "🚿 Urinate after sexual activity",
              "🧻 Always wipe front to back", "🚫 Avoid holding urine for too long",
              "👙 Wear breathable cotton underwear", "🥤 Avoid excessive caffeine and alcohol"]:
        st.markdown(f"- {t}")

    st.markdown('<div class="section-header">🏥 When to See a Doctor</div>', unsafe_allow_html=True)
    st.error("See a doctor immediately if you have: high fever, severe back pain, blood in urine, or symptoms lasting more than 2 days.")
    st.markdown("---")
    st.markdown('<div class="disclaimer">⚠️ For educational purposes only. Always consult a qualified healthcare professional.</div>', unsafe_allow_html=True)