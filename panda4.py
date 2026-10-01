import pandas as pd

data = {
    "Patient_ID": [101, 102, 103, 104, 105],
    "Patient_Name": ["Amit", "Neha", "Rahul", "Sneha", "Priya"],
    "Age": [65, 45, 72, 55, 68],
    "Disease": ["Diabetes", "Fever", "Heart Disease", "Cold", "Diabetes"],
    "Medical_Charges": [60000, 20000, 80000, 15000, 55000]
}

df = pd.DataFrame(data)

print("Patients above 60 years:")
print(df[df["Age"] > 60])

print("\nAverage Medical Charge:")
print(df["Medical_Charges"].mean())

print("\nMaximum Medical Charge:")
print(df["Medical_Charges"].max())

print("\nPatients with charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])