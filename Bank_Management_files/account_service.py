from models.customer import Customer
from models.account import Account
from utils.storage import load_data, save_data


class AccountService:

    def __init__(self):
        self.data = load_data()

    # -----------------------------------------
    # Create Account
    # -----------------------------------------
    def create_account(self):

        print("\n==========================================")
        print("             CREATE ACCOUNT")
        print("==========================================")

        customer_id = input("Enter Customer ID: ").strip()

        # Check if customer already has account
        for account in self.data["accounts"]:

            if account["customer_id"] == customer_id:

                print("\nThis customer already has an account.")
                print("Only ONE account is allowed per customer.")
                return

        # Check whether customer already exists
        existing_customer = None

        for customer in self.data["customers"]:

            if customer["customer_id"] == customer_id:

                existing_customer = customer
                break

        # If customer does not exist, create customer first
        if existing_customer is None:

            print("\nCustomer does not exist.")
            print("Please enter customer details.")

            name = input("Enter Name: ").strip()
            phone = input("Enter Phone: ").strip()
            email = input("Enter Email: ").strip()
            address = input("Enter Address: ").strip()
            pin = input("Create 4-digit PIN: ").strip()

            if len(pin) != 4 or not pin.isdigit():

                print("\nPIN must contain exactly 4 digits.")
                return

            customer = Customer(
                customer_id,
                name,
                phone,
                email,
                address,
                pin
            )

            customer_data = {
                "customer_id": customer.customer_id,
                "name": customer.name,
                "phone": customer.phone,
                "email": customer.email,
                "address": customer.address,
                "pin": customer.pin
            }

            self.data["customers"].append(customer_data)

        else:

            print("\nExisting customer found.")

        # Generate account number
        account_number = "ACC" + str(
            100001 + len(self.data["accounts"])
        )

        account = Account(
            account_number,
            customer_id,
            0
        )

        account_data = {
            "account_number": account.account_number,
            "customer_id": account.customer_id,
            "balance": account.balance,
            "withdrawal_limit": account.withdrawal_limit,
            "withdrawn_today": account.withdrawn_today
        }

        self.data["accounts"].append(account_data)

        save_data(self.data)

        print("\n==========================================")
        print("       ACCOUNT CREATED SUCCESSFULLY")
        print("==========================================")
        print("Customer ID   :", customer_id)
        print("Account Number:", account_number)
        print("Balance       : ₹0")
        print("Withdrawal Limit: ₹20,000")
        print("==========================================")


    # -----------------------------------------
    # Show Account
    # -----------------------------------------
    def show_account(self):

        print("\n==========================================")
        print("             ACCOUNT DETAILS")
        print("==========================================")

        customer_id = input("Enter Customer ID: ").strip()

        for account in self.data["accounts"]:

            if account["customer_id"] == customer_id:

                print("\nAccount Number :", account["account_number"])
                print("Customer ID    :", account["customer_id"])
                print("Balance        : ₹", account["balance"])
                print(
                    "Daily Withdrawal Limit: ₹",
                    account["withdrawal_limit"]
                )

                print("==========================================")
                return

        print("\nAccount not found.")


    # -----------------------------------------
    # Deposit Money
    # -----------------------------------------
    def deposit_money(self):

        print("\n==========================================")
        print("             DEPOSIT MONEY")
        print("==========================================")

        customer_id = input("Enter Customer ID: ").strip()

        for account in self.data["accounts"]:

            if account["customer_id"] == customer_id:

                try:
                    amount = float(input("Enter Amount: ₹"))

                except ValueError:
                    print("\nPlease enter a valid amount.")
                    return

                if amount <= 0:
                    print("\nAmount must be greater than zero.")
                    return

                account["balance"] += amount

                save_data(self.data)

                print("\nAmount deposited successfully.")
                print("Current Balance: ₹", account["balance"])
                return

        print("\nAccount not found.")


    # -----------------------------------------
    # Withdraw Money
    # -----------------------------------------
    def withdraw_money(self):

        print("\n==========================================")
        print("             WITHDRAW MONEY")
        print("==========================================")

        customer_id = input("Enter Customer ID: ").strip()

        for account in self.data["accounts"]:

            if account["customer_id"] == customer_id:

                try:
                    amount = float(input("Enter Amount: ₹"))

                except ValueError:
                    print("\nPlease enter a valid amount.")
                    return

                if amount <= 0:

                    print("\nAmount must be greater than zero.")
                    return

                if amount > account["balance"]:

                    print("\nInsufficient balance.")
                    return

                if (
                    account["withdrawn_today"] + amount
                    > account["withdrawal_limit"]
                ):

                    print("\nDaily withdrawal limit exceeded.")
                    print(
                        "Daily Limit: ₹",
                        account["withdrawal_limit"]
                    )

                    print(
                        "Already Withdrawn Today: ₹",
                        account["withdrawn_today"]
                    )

                    return

                account["balance"] -= amount
                account["withdrawn_today"] += amount

                save_data(self.data)

                print("\nAmount withdrawn successfully.")
                print("Current Balance: ₹", account["balance"])
                return

        print("\nAccount not found.")