from models.loan import Loan, LOAN_TYPES, display_loan_types
from utils.storage import load_data, save_data


class LoanService:

    def __init__(self):
        self.data = load_data()

    # -----------------------------------------
    # Display available loan types
    # -----------------------------------------
    def show_loan_types(self):

        display_loan_types()

    # -----------------------------------------
    # Apply for a loan
    # -----------------------------------------
    def apply_loan(self):

        print("\n==========================================")
        print("              APPLY FOR LOAN")
        print("==========================================")

        customer_id = input("Enter Customer ID: ").strip()

        # Check customer
        customer_exists = False

        for customer in self.data["customers"]:
            if customer["customer_id"] == customer_id:
                customer_exists = True
                break

        if not customer_exists:
            print("\nCustomer not found.")
            print("Please create an account first.")
            return

        # Display loan types
        self.show_loan_types()

        loan_names = list(LOAN_TYPES.keys())

        try:
            choice = int(input("\nSelect Loan Type (1-6): "))

            if choice < 1 or choice > len(loan_names):
                print("\nInvalid loan type.")
                return

        except ValueError:
            print("\nPlease enter a valid number.")
            return

        loan_type = loan_names[choice - 1]
        details = LOAN_TYPES[loan_type]

        print("\nSelected Loan :", loan_type)
        print("Interest Rate :", details["interest_rate"], "%")
        print("Maximum Tenure:", details["max_tenure"], "years")

        # Loan amount
        try:
            amount = float(input("\nEnter Loan Amount: ₹"))

        except ValueError:
            print("\nPlease enter a valid amount.")
            return

        if amount < details["min_amount"]:
            print("\nLoan amount is below the minimum limit.")
            print("Minimum Amount: ₹", details["min_amount"])
            return

        if amount > details["max_amount"]:
            print("\nLoan amount exceeds the maximum limit.")
            print("Maximum Amount: ₹", details["max_amount"])
            return

        # Tenure
        try:
            tenure = int(input("Enter Loan Tenure (years): "))

        except ValueError:
            print("\nPlease enter a valid tenure.")
            return

        if tenure <= 0:
            print("\nTenure must be greater than 0.")
            return

        if tenure > details["max_tenure"]:
            print("\nTenure exceeds the maximum limit.")
            print("Maximum Tenure:", details["max_tenure"], "years")
            return

        # Generate loan ID
        loan_id = "LN" + str(1001 + len(self.data["loans"]))

        # Create loan object
        loan = Loan(
            loan_id,
            customer_id,
            loan_type,
            amount,
            details["interest_rate"],
            tenure,
            "Applied"
        )

        # Convert object into dictionary
        loan_data = {
            "loan_id": loan.loan_id,
            "customer_id": loan.customer_id,
            "loan_type": loan.loan_type,
            "amount": loan.amount,
            "interest_rate": loan.interest_rate,
            "tenure": loan.tenure,
            "status": loan.status
        }

        # Save loan
        self.data["loans"].append(loan_data)

        save_data(self.data)

        print("\n==========================================")
        print("        LOAN APPLICATION SUCCESSFUL")
        print("==========================================")
        print("Loan ID       :", loan_id)
        print("Customer ID   :", customer_id)
        print("Loan Type     :", loan_type)
        print("Amount        : ₹", amount)
        print("Interest Rate :", details["interest_rate"], "%")
        print("Tenure        :", tenure, "years")
        print("Status        : Applied")
        print("==========================================")


    # -----------------------------------------
    # View customer's loans
    # -----------------------------------------
    def view_loans(self):

        print("\n==========================================")
        print("              MY LOANS")
        print("==========================================")

        customer_id = input("Enter Customer ID: ").strip()

        found = False

        for loan_data in self.data["loans"]:

            if loan_data["customer_id"] == customer_id:

                found = True

                loan = Loan(
                    loan_data["loan_id"],
                    loan_data["customer_id"],
                    loan_data["loan_type"],
                    loan_data["amount"],
                    loan_data["interest_rate"],
                    loan_data["tenure"],
                    loan_data["status"]
                )

                loan.display_loan()

        if not found:
            print("\nNo loans found for this customer.")


    # -----------------------------------------
    # View all loans
    # -----------------------------------------
    def view_all_loans(self):

        print("\n==========================================")
        print("              ALL LOANS")
        print("==========================================")

        if len(self.data["loans"]) == 0:
            print("\nNo loans available.")
            return

        for loan_data in self.data["loans"]:

            loan = Loan(
                loan_data["loan_id"],
                loan_data["customer_id"],
                loan_data["loan_type"],
                loan_data["amount"],
                loan_data["interest_rate"],
                loan_data["tenure"],
                loan_data["status"]
            )

            loan.display_loan()