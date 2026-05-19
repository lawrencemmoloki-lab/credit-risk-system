import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle

# Load dataset
columns = [
    "checking_status","duration","credit_history","purpose","credit_amount",
    "savings_status","employment","installment_rate","personal_status",
    "other_debtors","residence_since","property","age","other_installment_plans",
    "housing","existing_credits","job","num_dependents","own_telephone",
    "foreign_worker","default_status"
]

df = pd.read_csv("data/german.data", sep=" ", header=None, names=columns)

# Target fix
df["default_status"] = df["default_status"].map({1: 0, 2: 1})

# Features (same as Streamlit)
X = df[["duration", "credit_amount", "age", "installment_rate", "existing_credits"]]
y = df["default_status"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model
pickle.dump(model, open("src/model.pkl", "wb"))

print("Model trained and saved successfully!")