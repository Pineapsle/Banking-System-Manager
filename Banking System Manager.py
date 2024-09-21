import random

class Account:
    def __init__(self, account_number, name, balance=0):
        # Store account number privately
        self._account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        # Deposit money into the account
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Withdraw money from the account
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")

    def display_balance(self):
        # Display the current balance of the account
        print(f"Account balance for {self.name} is: ${self.balance}")

    def get_account_number(self):
        # Return the private account number
        return self._account_number


class SavingsAccount(Account):
    def __init__(self, account_number, name, balance=0, interest_rate=0.02):
        # Initialize a savings account with an interest rate
        super().__init__(account_number, name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        # Calculate and add interest to the account balance
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: ${interest:.2f}. New balance: ${self.balance:.2f}")


class CheckingAccount(Account):
    def __init__(self, account_number, name, balance=0, withdrawal_limit=500):
        # Initialize a checking account with a withdrawal limit
        super().__init__(account_number, name, balance)
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):
        # Withdraw money while enforcing the withdrawal limit
        if amount > self.withdrawal_limit:
            print(f"Amount exceeds withdrawal limit of ${self.withdrawal_limit}.")
        else:
            super().withdraw(amount)


class Bank:
    def __init__(self):
        # Initialize a bank with an empty list of accounts
        self.accounts = []

    def generate_account_number(self):
        # Generate a unique random 10-digit account number
        while True:
            account_number = random.randint(1000000000, 9999999999)
            # Ensure the account number is unique
            if not any(account.get_account_number() == account_number for account in self.accounts):
                return account_number

    def create_account(self, account_type, name, initial_deposit=0):
        # Create a new account of a specified type
        if initial_deposit < 0:
            print("Initial deposit must be non-negative.")
            return
        account_number = self.generate_account_number()
        if account_type == 'savings':
            account = SavingsAccount(account_number, name, initial_deposit)
        elif account_type == 'checking':
            account = CheckingAccount(account_number, name, initial_deposit)
        else:
            print("Invalid account type.")
            return
        self.accounts.append(account)
        print(f"Account created for {name}. Account Number: {account.get_account_number()}")

    def find_account(self, account_number):
        # Find an account by its account number
        account_number = int(account_number)
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        print("Account not found.")
        return None

    def show_accounts(self):
        # Display all accounts in the bank
        if not self.accounts:
            print("No accounts found.")
            return
        for account in self.accounts:
            print(
                f"Account Number: {account.get_account_number()}, Name: {account.name}, Balance: ${account.balance:.2f}")


def main():
    # Main function to run the bank system
    bank = Bank()
    while True:
        print("\n--- Bank System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Show All Accounts")
        print("6. Add Interest to Savings Account")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            # Create a new account
            account_type = input("Enter account type (savings/checking): ").lower()
            name = input("Enter account holder's name: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            bank.create_account(account_type, name, initial_deposit)

        elif choice == '2':
            # Deposit money into an account
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)

        elif choice == '3':
            # Withdraw money from an account
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)

        elif choice == '4':
            # Check the balance of an account
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                account.display_balance()

        elif choice == '5':
            # Show all accounts in the bank
            bank.show_accounts()

        elif choice == '6':  # Option for adding interest
            # Add interest to a savings account
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if isinstance(account, SavingsAccount):  # Ensure it's a savings account
                account.add_interest()
            else:
                print("Interest can only be added to savings accounts.")

        elif choice == '7':
            # Exit the system
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()