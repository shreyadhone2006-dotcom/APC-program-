# Create attendance file

with open("attendance.txt", "w") as file:
    file.write("RollNo,Name,Present,Total\n")
    file.write("101,Shreya,80,100\n")
    file.write("102,Gauri,90,100\n")
    file.write("103,Minal,65,100\n")


print("Students with attendance below 75%:")

with open("attendance.txt", "r") as file:
    next(file)

    for line in file:
        roll, name, present, total = line.strip().split(",")

        present = int(present)
        total = int(total)

        percentage = (present / total) * 100

        print(name, ":", percentage, "%")

        if percentage < 75:
            print("Below 75%:", name)