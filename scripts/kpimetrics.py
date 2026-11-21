import pandas as pd

# Read datasets
patients = pd.read_csv(
    "output/cleaned_patients.csv"
)

appointments = pd.read_csv(
    "data/appointments.csv"
)

labs = pd.read_csv(
    "data/lab_results.csv"
)

billing = pd.read_csv(
    "data/billing.csv"
)

# KPI 1
avg_wait_time = round(
    appointments["wait_time_mins"].mean(),
    2
)

# KPI 2
total_patients = (
    patients["patient_id"]
    .nunique()
)

# KPI 3
total_appointments = (
    appointments["appointment_id"]
    .count()
)

# KPI 4
total_revenue = (
    billing["amount"]
    .sum()
)

# KPI 5
avg_bill_amount = round(
    billing["amount"]
    .mean(),
    2
)

# KPI 6
most_common_test = (
    labs["test_name"]
    .mode()[0]
)

# KPI 7
blood_sugar_risk = labs[
    (labs["test_name"] == "Blood Sugar")
    &
    (
        pd.to_numeric(
            labs["result"],
            errors="coerce"
        ) >= 140
    )
]

cholesterol_risk = labs[
    (labs["test_name"] == "Cholesterol")
    &
    (
        pd.to_numeric(
            labs["result"],
            errors="coerce"
        ) >= 200
    )
]

hba1c_risk = labs[
    (labs["test_name"] == "HbA1c")
    &
    (
        pd.to_numeric(
            labs["result"],
            errors="coerce"
        ) >= 6.5
    )
]

high_risk_patients = pd.concat(
    [
        blood_sugar_risk,
        cholesterol_risk,
        hba1c_risk
    ]
)["patient_id"].nunique()

# Create KPI DataFrame
kpi_df = pd.DataFrame({
    "metric": [
        "Average Wait Time",
        "Total Patients",
        "Total Appointments",
        "Total Revenue",
        "Average Billing Amount",
        "Most Frequent Test",
        "High Risk Patients"
    ],
    "value": [
        avg_wait_time,
        total_patients,
        total_appointments,
        total_revenue,
        avg_bill_amount,
        most_common_test,
        high_risk_patients
    ]
})

# Save KPI Metrics
kpi_df.to_csv(
    "output/patients_kpi_metrics.csv",
    index=False
)

print(
    "KPI metrics generated successfully"
)