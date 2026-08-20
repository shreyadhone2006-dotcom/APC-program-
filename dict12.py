students = {
    "Shreya": 80,
    "Shital": 95,
    "Supriya": 65,
    "Gauri": 92
}

lowest = min(students, key=students.get)

print("Lowest marks:", students[lowest])
print("Student:", lowest)