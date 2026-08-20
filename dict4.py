students = {
    "Shreya": 80,
    "Minal": 75,
    "Sayali": 90
}

name = input("Enter student name: ")
marks = int(input("Enter new marks: "))

if name in students:
    students[name] = marks
    print(students)
else:
    print("Student not found")