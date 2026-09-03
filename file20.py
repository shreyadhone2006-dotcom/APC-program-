# Create transaction file

with open("transactions.txt", "w") as file:
    file.write("Deposit,10000\n")
    file.write("Withdrawal,2000\n")
    file.write("Deposit,5000\n")
    file.write("Withdrawal,1500\n")


total_deposit = 0
total_withdrawal = 0
transactions = []

with open("transactions.txt", "r") as file:
    for line in file:
        transaction, amount = line.strip().split(",")

        amount = int(amount)
        transactions.append(amount)

        if transaction == "Deposit":
            total_deposit += amount

        elif transaction == "Withdrawal":
            total_withdrawal += amount


final_balance = total_deposit - total_withdrawal
largest_transaction = max(transactions)


print("Total Deposits:", total_deposit)
print("Total Withdrawals:", total_withdrawal)
print("Final Balance:", final_balance)
print("Largest Transaction:", largest_transaction)