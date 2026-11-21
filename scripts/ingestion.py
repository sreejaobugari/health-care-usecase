import pandas as pd

patients = pd.read_csv("data/patients.csv")
appointments = pd.read_csv("data/appointments.csv")
labs = pd.read_csv("data/lab_results.csv")
billing = pd.read_csv("data/billing.csv")

print("Datasets Loaded Successfully")