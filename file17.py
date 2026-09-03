# Create student records file

with open("students.txt", "w") as file:
    file.write("RollNo,Name,Marks\n")
    file.write("101,Gauri,85\n")
    file.write("102,Shreya,92\n")
    file.write("103,Ishita,78\n")


students = []

with open("students.txt", "r") as file:
    next(file)   # Skip header

    for line in file:
        roll, name, marks = line.strip().split(",")
        students.append((roll, name, int(marks)))


# Display all records
print("All Student Records:")

for student in students:
    print(student)


# Find highest marks
highest = max(students, key=lambda x: x[2])

print("\nStudent with highest marks:")
print(highest)


# Calculate average marks
total = sum(student[2] for student in students)
average = total / len(students)

print("\nAverage marks:", average)


# Students scoring more than 80
print("\nStudents scoring more than 80:")

for student in students:
    if student[2] > 80:
        print(student)