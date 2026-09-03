import salary

basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
deduction = float(input("Enter deduction: "))

gross = salary.gross_salary(basic, allowance)
ded = salary.deductions(gross, deduction)
net = salary.net_salary(gross, ded)

print("Gross Salary =", gross)
print("Deductions =", ded)
print("Net Salary =", net)