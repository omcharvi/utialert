
import pandas as pd
import random

# Set seed so data is same every time
random.seed(42)

# We'll create 500 fake patient records
data = []

for i in range(500):
    age = random.randint(15, 70)
    burning = random.randint(0, 1)
    frequent_urge = random.randint(0, 1)
    cloudy_urine = random.randint(0, 1)
    pelvic_pain = random.randint(0, 1)
    fever = random.randint(0, 1)
    blood_in_urine = random.randint(0, 1)
    back_pain = random.randint(0, 1)
    hydration = random.choice([0, 1, 2])  # 0=low, 1=moderate, 2=high
    history = random.randint(0, 1)

    # Count how many symptoms the person has
    symptom_count = (burning + frequent_urge + cloudy_urine +
                     pelvic_pain + fever + blood_in_urine + back_pain)

    # Rule: more symptoms + low hydration + history = more likely UTI
    score = symptom_count * 0.4 + (1 - hydration * 0.4) + history * 0.5
    uti_positive = 1 if score > 1.5 else 0

    data.append({
        "age": age,
        "burning": burning,
        "frequent_urge": frequent_urge,
        "cloudy_urine": cloudy_urine,
        "pelvic_pain": pelvic_pain,
        "fever": fever,
        "blood_in_urine": blood_in_urine,
        "back_pain": back_pain,
        "hydration": hydration,
        "history": history,
        "uti_positive": uti_positive
    })

# Save to CSV file
df = pd.DataFrame(data)
df.to_csv("data/uti_data.csv", index=False)

print("✅ Dataset created! Total records:", len(df))
print("UTI Positive cases:", df["uti_positive"].sum())
print("UTI Negative cases:", (df["uti_positive"] == 0).sum())