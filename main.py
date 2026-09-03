import student

marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = float(input("Enter marks: "))
    marks.append(mark)

total = student.total_marks(marks)
per = student.percentage(marks)
g = student.grade(per)

print("\nStudent Result")
print("Total Marks =", total)
print("Percentage =", per)
print("Grade =", g)