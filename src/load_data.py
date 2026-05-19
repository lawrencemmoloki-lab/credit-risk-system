import pandas as pd
from connect_db import engine

#  Load Dataset
columns = [
    "checking_status", "duration", "credit_history", "purpose", "credit_amount",
    "savings_status", "employment", "installment_rate", "personal_status",
    "other_debtors", "residence_since", "property", "age", "other_installment_plans",
    "housing", "existing_credits", "job", "num_dependents", "own_telephone",
    "foreign_worker", "default_status"
]

df = pd.read_csv(
    "data/german.data",
    sep=' ',
    header=None,
    names=columns
)

#  Convert Target Variable
df["default_status"] = df["default_status"].map({1: 0, 2: 1})

# STEP 17: Create Customer Table
customers_df = df[["age", "housing", "job"]].copy()
customers_df["sex"] = "unknown"
customers_df.insert(0, "customer_id", range(1, len(customers_df) + 1))

# STEP 18: Create Loans Table
loans_df = df[[
    "checking_status", "duration", "credit_history", "purpose", "credit_amount",
    "savings_status", "employment", "installment_rate", "default_status"
]].copy()

loans_df.insert(0, "customer_id", customers_df["customer_id"].values)

# STEP 19: Upload to PostgreSQL
try:
    print("Uploading customers...")
    customers_df.to_sql("customers", engine, if_exists="replace", index=False)

    print("Uploading loans...")
    loans_df.to_sql("loans", engine, if_exists="replace", index=False)

    print("Data uploaded successfully!")

except Exception as e:
    print("Upload failed:")
    print(e)