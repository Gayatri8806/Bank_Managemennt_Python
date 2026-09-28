from models.card import Card
from utils.storage import load_data, save_data
from datetime import datetime, timedelta


class CardService:

    def __init__(self):
        self.data = load_data()

    # -----------------------------------------
    # Check whether customer exists
    # -----------------------------------------
    def customer_exists(self, customer_id):

        for customer in self.data["customers"]:

            if customer["customer_id"] == customer_id:
                return True

        return False

    # -----------------------------------------
    # Generate dummy card number
    # -----------------------------------------
    def generate_card_number(self):

        card_number = "XXXX-XXXX-XXXX-" + str(
            1000 + len(self.data["cards"]) + 1
        )

        return card_number

    # -----------------------------------------
    # Generate expiry date
    # -----------------------------------------
    def generate_expiry_date(self):

        expiry = datetime.now() + timedelta(days=5 * 365)

        return expiry.strftime("%m/%Y")

    # -----------------------------------------
    # Issue Debit Card
    # -----------------------------------------
    def issue_debit_card(self):

        print("\n==========================================")
        print("            ISSUE DEBIT CARD")
        print("==========================================")

        customer_id = input("Enter Customer ID: ").strip()

        if not self.customer_exists(customer_id):

            print("\nCustomer not found.")
            print("Please create an account first.")
            return

        # Check existing debit card
        for card in self.data["cards"]:

            if (
                card["customer_id"] == customer_id
                and card["card_type"] == "Debit Card"
            ):

                print("\nDebit Card already exists for this customer.")
                return

        card_number = self.generate_card_number()
        expiry_date = self.generate_expiry_date()

        card = Card(
            card_number,
            customer_id,
            "Debit Card",
            expiry_date,
            "Active"
        )

        card_data = {
            "card_number": card.card_number,
            "customer_id": card.customer_id,
            "card_type": card.card_type,
            "expiry_date": card.expiry_date,
            "status": card.status,
            "credit_limit": 0,
            "available_credit": 0
        }

        self.data["cards"].append(card_data)

        save_data(self.data)

        print("\n==========================================")
        print("        DEBIT CARD ISSUED SUCCESSFULLY")
        print("==========================================")
        print("Card Number :", card_number)
        print("Customer ID :", customer_id)
        print("Expiry Date :", expiry_date)
        print("Status      : Active")
        print("==========================================")


    # -----------------------------------------
    # Issue Credit Card
    # -----------------------------------------
    def issue_credit_card(self):

        print("\n==========================================")
        print("            ISSUE CREDIT CARD")
        print("==========================================")

        customer_id = input("Enter Customer ID: ").strip()

        if not self.customer_exists(customer_id):

            print("\nCustomer not found.")
            print("Please create an account first.")
            return

        # Check existing credit card
        for card in self.data["cards"]:

            if (
                card["customer_id"] == customer_id
                and card["card_type"] == "Credit Card"
            ):

                print("\nCredit Card already exists for this customer.")
                return

        try:

            credit_limit = float(
                input("Enter Credit Limit: ₹")
            )

        except ValueError:

            print("\nPlease enter a valid amount.")
            return

        if credit_limit <= 0:

            print("\nCredit limit must be greater than zero.")
            return

        card_number = self.generate_card_number()
        expiry_date = self.generate_expiry_date()

        card = Card(
            card_number,
            customer_id,
            "Credit Card",
            expiry_date,
            "Active",
            credit_limit,
            credit_limit
        )

        card_data = {
            "card_number": card.card_number,
            "customer_id": card.customer_id,
            "card_type": card.card_type,
            "expiry_date": card.expiry_date,
            "status": card.status,
            "credit_limit": card.credit_limit,
            "available_credit": card.available_credit
        }

        self.data["cards"].append(card_data)

        save_data(self.data)

        print("\n==========================================")
        print("       CREDIT CARD ISSUED SUCCESSFULLY")
        print("==========================================")
        print("Card Number     :", card_number)
        print("Customer ID     :", customer_id)
        print("Credit Limit    : ₹", credit_limit)
        print("Available Credit: ₹", credit_limit)
        print("Expiry Date     :", expiry_date)
        print("Status          : Active")
        print("==========================================")


    # -----------------------------------------
    # View customer cards
    # -----------------------------------------
    def view_cards(self):

        print("\n==========================================")
        print("               MY CARDS")
        print("==========================================")

        customer_id = input("Enter Customer ID: ").strip()

        found = False

        for card_data in self.data["cards"]:

            if card_data["customer_id"] == customer_id:

                found = True

                card = Card(
                    card_data["card_number"],
                    card_data["customer_id"],
                    card_data["card_type"],
                    card_data["expiry_date"],
                    card_data["status"],
                    card_data["credit_limit"],
                    card_data["available_credit"]
                )

                card.display_card()

        if not found:

            print("\nNo cards found for this customer.")


    # -----------------------------------------
    # Block a card
    # -----------------------------------------
    def block_card(self):

        print("\n==========================================")
        print("               BLOCK CARD")
        print("==========================================")

        card_number = input("Enter Card Number: ").strip()

        found = False

        for card_data in self.data["cards"]:

            if card_data["card_number"] == card_number:

                found = True

                if card_data["status"] == "Blocked":

                    print("\nCard is already blocked.")
                    return

                card_data["status"] = "Blocked"

                save_data(self.data)

                print("\nCard blocked successfully.")
                return

        if not found:

            print("\nCard not found.")


    # -----------------------------------------
    # Activate a card
    # -----------------------------------------
    def activate_card(self):

        print("\n==========================================")
        print("             ACTIVATE CARD")
        print("==========================================")

        card_number = input("Enter Card Number: ").strip()

        found = False

        for card_data in self.data["cards"]:

            if card_data["card_number"] == card_number:

                found = True

                if card_data["status"] == "Active":

                    print("\nCard is already active.")
                    return

                card_data["status"] = "Active"

                save_data(self.data)

                print("\nCard activated successfully.")
                return

        if not found:

            print("\nCard not found.")