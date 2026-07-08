import pandas as pd
import joblib
from pathlib import Path
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

print("__file__ =", __file__)
BASE_DIR = Path(__file__).resolve().parent
print("BASE_DIR =", BASE_DIR)
MODELS_DIR = BASE_DIR / "Models"

df = pd.read_csv("D:\GITHUB REPOs\GEN-AI\Projects\ResumeShortlister\Training Data\candidates.csv")

df["Degree"] = df["Degree"].str.strip().str.lower()
df["Selected"] = df["Selected"].str.strip().str.lower()

degree_encoder = LabelEncoder()
target_encoder = LabelEncoder()

df["Degree"] = degree_encoder.fit_transform(df["Degree"])
df["Selected"] = target_encoder.fit_transform(df["Selected"])

X = df.drop(columns=["Name", "Selected"])
joblib.dump(list(X.columns), MODELS_DIR / "feature_columns.pkl")

y = df["Selected"]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

joblib.dump(model, "D:/GITHUB REPOs/GEN-AI/Projects/ResumeShortlister/Models/resume_model.pkl")
joblib.dump(degree_encoder, "D:/GITHUB REPOs/GEN-AI/Projects/ResumeShortlister/Models/degree_encoder.pkl")
joblib.dump(target_encoder, "D:/GITHUB REPOs/GEN-AI/Projects/ResumeShortlister/Models/target_encoder.pkl")

print("Model Trained Successfully")
