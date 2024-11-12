class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        """
        Initialize a BankAccount object with the given attributes.
        """
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit the given amount into the account and return the amount deposited.
        """
        self.balance += amount
        return amount

    def withdraw(self, amount):
        """
        Withdraw the given amount from the account if sufficient balance is available.
        Return 'Insufficient balance' if the account balance is less than the amount to be withdrawn.
        Otherwise, return the amount withdrawn.
        """
        if self.balance < amount:
            return 'Insufficient balance'
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        """
        Print the current balance of the account.
        """
        print(f"Current balance: {self.balance}")

    def customer_details(self):
        """
        Print the customer's details, including name, account number, date of account opening, and balance.
        """
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Account Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")