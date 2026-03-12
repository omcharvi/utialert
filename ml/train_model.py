
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

# ── Step 1: Load the data ──────────────────────────────
df = pd.read_csv("data/uti_data.csv")
print("✅ Data loaded! Shape:", df.shape)

# ── Step 2: Split into inputs (X) and answer (y) ──────
# X = everything the model learns FROM
# y = what the model is trying to PREDICT
X = df.drop("uti_positive", axis=1)
y = df["uti_positive"]

# ── Step 3: Split into training and testing sets ───────
# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

# ── Step 4: Create and train the model ────────────────
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("✅ Model trained!")

# ── Step 5: Test how accurate it is ───────────────────
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {accuracy * 100:.2f}%")
print("\nDetailed Report:")
print(classification_report(y_test, y_pred))

# ── Step 6: Save the model ────────────────────────────
joblib.dump(model, "ml/model.pkl")
print("✅ Model saved to ml/model.pkl")