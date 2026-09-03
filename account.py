def create_account(name, balance):
    account = {
        "name": name,
        "balance": balance
    }

    return account


def check_balance(account):
    return account["balance"]