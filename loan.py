def calculate_loan(principal, rate, years):
    interest = (principal * rate * years) / 100

    total = principal + interest

    return total