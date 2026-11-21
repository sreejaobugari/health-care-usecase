import pandas as pd
import numpy as np

patients = pd.read_csv("data/patients.csv")

# Standardize Patient IDs
patients["patient_id"] = (
    patients["patient_id"]
    .str.upper()
    .str.replace("PAT_", "P", regex=False)
    .str.replace("PAT", "P", regex=False)
)

# Convert names to uppercase
patients["name"] = patients["name"].str.upper()

# Convert addresses to lowercase
patients["address"] = patients["address"].str.lower()

# Replace empty strings and spaces with NaN
patients = patients.replace(r'^\s*$', np.nan, regex=True)

# Standardize phone numbers
patients["phone"] = (
    patients["phone"]
    .astype("string")
    .str.replace("+91", "", regex=False)
    .str.replace(" ", "", regex=False)
    .str.replace("-", "", regex=False)
)

patients.to_csv(
    "output/standardized_patients.csv",
    index=False
)

print("Patient data standardized successfully")