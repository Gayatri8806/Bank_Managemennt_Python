class Loan:

    def __init__(
        self,
        loan_id,
        customer_id,
        loan_type,
        amount,
        interest_rate,
        tenure,
        status="Applied"
    ):
        self.loan_id = loan_id
        self.customer_id = customer_id
        self.loan_type = loan_type
        self.amount = amount
        self.interest_rate = interest_rate
        self.tenure = tenure
        self.status = status

    def display_loan(self):
        print("\n==========================================")
        print("              LOAN DETAILS")
        print("==========================================")
        print("Loan ID          :", self.loan_id)
        print("Customer ID      :", self.customer_id)
        print("Loan Type        :", self.loan_type)
        print("Loan Amount      : ₹", self.amount)
        print("Interest Rate    :", self.interest_rate, "%")
        print("Tenure           :", self.tenure, "years")
        print("Status           :", self.status)
        print("==========================================")


# Loan types available in our banking system
# These are project/demo values.

LOAN_TYPES = {

    "Personal Loan": {
        "min_amount": 50000,
        "max_amount": 1000000,
        "interest_rate": 11.0,
        "max_tenure": 5
    },

    "Home Loan": {
        "min_amount": 500000,
        "max_amount": 5000000,
        "interest_rate": 8.5,
        "max_tenure": 20
    },

    "Education Loan": {
        "min_amount": 50000,
        "max_amount": 2000000,
        "interest_rate": 7.5,
        "max_tenure": 10
    },

    "Car Loan": {
        "min_amount": 100000,
        "max_amount": 2000000,
        "interest_rate": 9.0,
        "max_tenure": 7
    },

    "Business Loan": {
        "min_amount": 100000,
        "max_amount": 5000000,
        "interest_rate": 12.0,
        "max_tenure": 10
    },

    "Gold Loan": {
        "min_amount": 20000,
        "max_amount": 1000000,
        "interest_rate": 10.0,
        "max_tenure": 5
    }
}


def display_loan_types():

    print("\n==========================================")
    print("          AVAILABLE LOAN TYPES")
    print("==========================================")

    number = 1

    for loan_name, details in LOAN_TYPES.items():

        print("\n", number, ".", loan_name)
        print("   Minimum Amount : ₹", details["min_amount"])
        print("   Maximum Amount : ₹", details["max_amount"])
        print("   Interest Rate  :", details["interest_rate"], "%")
        print("   Maximum Tenure :", details["max_tenure"], "years")

        number += 1

    print("\n==========================================")