import pandas as pd

# Read curated patient data
patients = pd.read_csv(
    "output/standardized_patients.csv"
)

# Replace all missing values with UNKNOWN
patients = patients.fillna("UNKNOWN")

# Save cleaned dataset
patients.to_csv(
    "output/cleaned_patients.csv",
    index=False
)

print("Patients data cleansed successfully")