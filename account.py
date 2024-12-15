
import json
import os

class Account:
    DATA_FILE = "accounts.json"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited {amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew {amount}")
            return True
        return False

    def get_balance(self):
        return self.balance

    def show_history(self):
        if not self.history:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for h in self.history:
                print("-", h)

    def to_dict(self):
        return {
            "owner": self.owner,
            "balance": self.balance,
            "history": self.history
        }

    @classmethod
    def save_accounts(cls, accounts):
        data = {acc.owner: acc.to_dict() for acc in accounts}
        with open(cls.DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load_accounts(cls):
        if not os.path.exists(cls.DATA_FILE):
            return []
        with open(cls.DATA_FILE, "r") as f:
            data = json.load(f)
        accounts = []
        for owner, info in data.items():
            acc = Account(owner, info["balance"])
            acc.history = info.get("history", [])
            accounts.append(acc)
        return accounts