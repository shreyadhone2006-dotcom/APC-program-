marks = []
for i in range(20):
    m = float(input("Enter marks of student " + str(i + 1) + ": "))
    marks.append(m)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above = 0
below = 0

for m in marks:
    if m > average:
        above += 1
    elif m < average:
        below += 1

print("\nHighest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Students Above Average:", above)
print("Students Below Average:", below)