employees = {
    101: "Shreya",
    102: "Sayali",
    103: "Minal",
    104: "Gauri"
}

id = int(input("Enter employee ID: "))

if id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")