
def deposit(account, amount):
    if account.deposit(amount):
        print(f"Deposited {amount}. New balance: {account.get_balance()}")
    else:
        print("Deposit failed. Amount must be positive.")

def withdraw(account, amount):
    if account.withdraw(amount):
        print(f"Withdrew {amount}. New balance: {account.get_balance()}")
    else:
        print("Withdrawal failed. Check balance or amount.")

def check_balance(account):
    print(f"{account.owner}'s current balance: {account.get_balance()}")

def transaction_history(account):
    account.show_history()