class Account:

    def __init__(self, account_number, customer_id, balance=0):
        self.account_number = account_number
        self.customer_id = customer_id
        self.balance = balance

        # Maximum amount that can be withdrawn in one day
        self.withdrawal_limit = 20000

        # Amount already withdrawn today
        self.withdrawn_today = 0

    def deposit(self, amount):

        if amount <= 0:
            print("\nInvalid deposit amount.")
            return False

        self.balance += amount

        print("\nAmount deposited successfully.")
        print("Current Balance: ₹", self.balance)

        return True

    def withdraw(self, amount):

        if amount <= 0:
            print("\nInvalid withdrawal amount.")
            return False

        if amount > self.balance:
            print("\nInsufficient balance.")
            return False

        if self.withdrawn_today + amount > self.withdrawal_limit:
            print("\nDaily withdrawal limit exceeded.")
            print("Daily Limit: ₹", self.withdrawal_limit)
            print("Already Withdrawn Today: ₹", self.withdrawn_today)
            return False

        self.balance -= amount
        self.withdrawn_today += amount

        print("\nAmount withdrawn successfully.")
        print("Current Balance: ₹", self.balance)

        return True

    def check_balance(self):

        print("\n========== ACCOUNT BALANCE ==========")
        print("Account Number :", self.account_number)
        print("Balance        : ₹", self.balance)
        print("Withdrawal Limit: ₹", self.withdrawal_limit)
        print("=====================================")

    def display_account(self):

        print("\n========== ACCOUNT DETAILS ==========")
        print("Account Number :", self.account_number)
        print("Customer ID    :", self.customer_id)
        print("Balance        : ₹", self.balance)
        print("Daily Withdrawal Limit: ₹", self.withdrawal_limit)
        print("=====================================")