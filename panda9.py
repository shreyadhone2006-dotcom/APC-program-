import pandas as pd

salary = {
    "Shreya": 75000,
    "Dhiraj": 60000,
    "Sayali": 45000,
    "Minal": 48000,
    "Abhi": 80000
}

s = pd.Series(salary)

print("Series:")
print(s)

print("\nHighest Salary:")
print(s.max())

print("\nLowest Salary:")
print(s.min())

print("\nAverage Salary:")
print(s.mean())

print("\nEmployees earning more than 50000:")
print(s[s > 50000])