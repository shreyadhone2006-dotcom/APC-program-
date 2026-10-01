import pandas as pd

ages = {
    "Patient1": 45,
    "Patient2": 65,
    "Patient3": 72,
    "Patient4": 55,
    "Patient5": 68
}

s = pd.Series(ages)

print("Average Age:")
print(s.mean())

print("\nOldest Patient:")
print(s.idxmax(), s.max())

print("\nYoungest Patient:")
print(s.idxmin(), s.min())

print("\nPatients above 60:")
print(s[s > 60])