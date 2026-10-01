import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Employee_Name": ["Shreya", "Sayali", "Minal", "Dipali", "Gauri"],
    "Department": ["CSE", "IT", "IT", "ENTC", "CSE"],
    "Salary": [85000, 40000, 75000, 50000, 80000],
    "Experience": [2, 5, 7, 3, 8]
}

df = pd.DataFrame(data)

print("Employees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nEmployee with highest experience:")
print(df.loc[df["Experience"].idxmax()])