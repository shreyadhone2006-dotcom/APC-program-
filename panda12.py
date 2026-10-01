import pandas as pd

attendance = {
    "Shreya": 85,
    "Minal": 72,
    "Sayali": 95,
    "Dipali": 68,
    "Diksha": 92
}

s = pd.Series(attendance)

print("Average Attendance:")
print(s.mean())

print("\nStudents below 75%:")
print(s[s < 75])

print("\nStudents above 90%:")
print(s[s > 90])

print("\nHighest Attendance:")
print(s.max())