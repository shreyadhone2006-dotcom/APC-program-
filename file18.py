# Create employee file

with open("employees.txt", "w") as file:
    file.write("ID,Name,Department,Salary\n")
    file.write("101,Shreya,IT,50000\n")
    file.write("102,Minal,HR,60000\n")
    file.write("103,Sayali,Sales,45000\n")


employees = []

with open("employees.txt", "r") as file:
    next(file)

    for line in file:
        emp_id, name, dept, salary = line.strip().split(",")
        employees.append((emp_id, name, dept, int(salary)))


def display_employees():
    print("All Employees:")
    for emp in employees:
        print(emp)


def highest_paid():
    employee = max(employees, key=lambda x: x[3])
    print("\nHighest Paid Employee:")
    print(employee)


def average_salary():
    total = sum(emp[3] for emp in employees)
    average = total / len(employees)
    print("\nAverage Salary:", average)


def above_salary(amount):
    print("\nEmployees earning above", amount)

    for emp in employees:
        if emp[3] > amount:
            print(emp)


display_employees()
highest_paid()
average_salary()

salary = int(input("\nEnter salary limit: "))
above_salary(salary)