from services.customer_service import CustomerService
from services.account_service import AccountService
from services.loan_service import LoanService
from services.card_service import CardService


# ==========================================
# CREATE SERVICE OBJECTS
# ==========================================

customer_service = CustomerService()
account_service = AccountService()
loan_service = LoanService()
card_service = CardService()


# ==========================================
# CUSTOMER MANAGEMENT
# ==========================================

def customer_menu():

    while True:

        print("\n")
        print("==========================================")
        print("         CUSTOMER MANAGEMENT")
        print("==========================================")
        print("1. Add Customer")
        print("2. View Customer")
        print("3. View All Customers")
        print("4. Back to Main Menu")
        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            customer_service.add_customer()

        elif choice == "2":

            customer_service.view_customer()

        elif choice == "3":

            customer_service.view_all_customers()

        elif choice == "4":

            break

        else:

            print("\nInvalid choice. Please try again.")


# ==========================================
# ACCOUNT MANAGEMENT
# ==========================================

def account_menu():

    while True:

        print("\n")
        print("==========================================")
        print("          ACCOUNT MANAGEMENT")
        print("==========================================")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Back to Main Menu")
        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            account_service.create_account()

        elif choice == "2":

            account_service.show_account()

        elif choice == "3":

            account_service.deposit_money()

        elif choice == "4":

            account_service.withdraw_money()

        elif choice == "5":

            break

        else:

            print("\nInvalid choice. Please try again.")


# ==========================================
# LOAN MANAGEMENT
# ==========================================

def loan_menu():

    while True:

        print("\n")
        print("==========================================")
        print("             LOAN MANAGEMENT")
        print("==========================================")
        print("1. View Loan Types")
        print("2. Apply for Loan")
        print("3. View My Loans")
        print("4. View All Loans")
        print("5. Back to Main Menu")
        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            loan_service.show_loan_types()

        elif choice == "2":

            loan_service.apply_loan()

        elif choice == "3":

            loan_service.view_loans()

        elif choice == "4":

            loan_service.view_all_loans()

        elif choice == "5":

            break

        else:

            print("\nInvalid choice. Please try again.")


# ==========================================
# CARD MANAGEMENT
# ==========================================

def card_menu():

    while True:

        print("\n")
        print("==========================================")
        print("             CARD MANAGEMENT")
        print("==========================================")
        print("1. Issue Debit Card")
        print("2. Issue Credit Card")
        print("3. View My Cards")
        print("4. Block Card")
        print("5. Activate Card")
        print("6. Back to Main Menu")
        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            card_service.issue_debit_card()

        elif choice == "2":

            card_service.issue_credit_card()

        elif choice == "3":

            card_service.view_cards()

        elif choice == "4":

            card_service.block_card()

        elif choice == "5":

            card_service.activate_card()

        elif choice == "6":

            break

        else:

            print("\nInvalid choice. Please try again.")


# ==========================================
# MAIN MENU
# ==========================================

def main_menu():

    while True:

        print("\n\n")
        print("==========================================")
        print("       BANKING MANAGEMENT SYSTEM")
        print("==========================================")
        print("1. Customer Management")
        print("2. Account Management")
        print("3. Loan Management")
        print("4. Card Management")
        print("5. Exit")
        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":

            customer_menu()

        elif choice == "2":

            account_menu()

        elif choice == "3":

            loan_menu()

        elif choice == "4":

            card_menu()

        elif choice == "5":

            print("\n==========================================")
            print("   Thank you for using Banking System!")
            print("==========================================")

            break

        else:

            print("\nInvalid choice. Please enter 1-5.")


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":

    main_menu()