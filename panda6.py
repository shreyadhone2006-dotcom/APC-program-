import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Shreya", "Dhiraj", "Ishita", "Viraj", "ShreyaC"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "IT"],
    "Total_Classes": [100, 100, 120, 90, 110],
    "Classes_Attended": [90, 82, 80, 55, 60]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print("DataFrame:")
print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])