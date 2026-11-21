import pandas as pd

# Read cleaned patient data
patients = pd.read_csv(
    "output/cleaned_patients.csv"
)

# Mask patient name
patients["name"] = "MASKED"

# Mask phone number
patients["phone"] = "XXXXXXXXXX"

# Mask address
patients["address"] = "MASKED"

# Save masked dataset
patients.to_csv(
    "output/masked_patients.csv",
    index=False
)

print("Patient data masked successfully")