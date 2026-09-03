from students.marks import total, percentage
from students.grade import calculate_grade
from students.attendance import attendance_percentage, eligibility

marks = [80, 85, 90, 75, 88]

present = 80
total_classes = 100

total_marks = total(marks)
per = percentage(marks)

print("Student Report")
print("Total Marks =", total_marks)
print("Percentage =", per)
print("Grade =", calculate_grade(per))

attendance = attendance_percentage(present, total_classes)

print("Attendance =", attendance, "%")
print("Eligibility =", eligibility(present, total_classes))