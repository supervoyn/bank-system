
from account import Account
from bank_operations import deposit, withdraw, check_balance, transaction_history

def main():
    print("Welcome to Advanced Bank System")
    accounts = Account.load_accounts()

    while True:
        print("\nOptions:")
        print("1. Create account")
        print("2. Select account")
        print("3. Exit")

        choice = input("Choose option (1-3): ")

        if choice == "1":
            owner = input("Enter your name: ")
            if any(acc.owner == owner for acc in accounts):
                print("Account already exists.")
            else:
                acc = Account(owner)
                accounts.append(acc)
                print(f"Account for {owner} created.")
        elif choice == "2":
            owner = input("Enter account name: ")
            acc = next((a for a in accounts if a.owner == owner), None)
            if not acc:
                print("Account not found.")
                continue

            while True:
                print(f"\nAccount: {acc.owner}")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Transaction History")
                print("5. Back to main menu")

                option = input("Choose option (1-5): ")

                if option == "1":
                    amount = float(input("Enter deposit amount: "))
                    deposit(acc, amount)
                elif option == "2":
                    amount = float(input("Enter withdrawal amount: "))
                    withdraw(acc, amount)
                elif option == "3":
                    check_balance(acc)
                elif option == "4":
                    transaction_history(acc)
                elif option == "5":
                    break
                else:
                    print("Invalid option.")

        elif choice == "3":
            Account.save_accounts(accounts)
            print("All accounts saved. Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()