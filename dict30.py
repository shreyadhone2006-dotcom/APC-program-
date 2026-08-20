students = {
    "Shreya": "Computer",
    "Gauri": "IT",
    "Sayali": "Computer",
    "Minal": "ENTC",
    "Riya": "IT"
}

departments = {}

for name, department in students.items():
    if department not in departments:
        departments[department] = []

    departments[department].append(name)

print(departments)