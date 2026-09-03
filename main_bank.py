from banking.account import create_account, check_balance
from banking.transaction import deposit, withdraw
from banking.loan import calculate_loan

account = create_account("Shreya", 10000)

deposit(account, 5000)

withdraw(account, 2000)

print("Account Holder:", account["name"])
print("Balance:", check_balance(account))

loan = calculate_loan(100000, 8, 2)

print("Total Loan Amount:", loan)