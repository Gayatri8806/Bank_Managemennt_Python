from datetime import datetime


class Transaction:

    def __init__(self, transaction_id, account_number, transaction_type, amount, balance):
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance = balance
        self.date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def display_transaction(self):

        print("\n--------------------------------------")
        print("Transaction ID :", self.transaction_id)
        print("Account Number  :", self.account_number)
        print("Type            :", self.transaction_type)
        print("Amount          : ₹", self.amount)
        print("Balance         : ₹", self.balance)
        print("Date & Time     :", self.date_time)
        print("--------------------------------------")