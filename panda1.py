import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Student_Name": ["Shreya", "Gauri", "Ishita", "Abhi", "Dhiraj"],
    "Python": [92, 70, 90, 65, 85],
    "DBMS": [89, 80, 88, 70, 90],
    "Mathematics": [90, 75, 92, 68, 80]}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Mathematics"]

df["Average"] = df["Total"] / 3

print("\nTotal and Average:")
print(df)

print("\nStudents with average more than 75:")
print(df[df["Average"] > 75])