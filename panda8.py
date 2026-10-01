import pandas as pd

marks = {
    "Shreya": 80,
    "Sayali": 72,
    "Gauri": 90,
    "Kasturi": 65,
    "Minal": 85
}

s = pd.Series(marks)

print("Series:")
print(s)

print("\nMarks of Shreya:")
print(s["Shreya"])

print("\nMaximum Marks:")
print(s.max())

print("\nMinimum Marks:")
print(s.min())

print("\nAverage Marks:")
print(s.mean())

print("\nStudents scoring more than 75:")
print(s[s > 75])