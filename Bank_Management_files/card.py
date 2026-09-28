class Card:

    def __init__(
        self,
        card_number,
        customer_id,
        card_type,
        expiry_date,
        status="Active",
        credit_limit=0,
        available_credit=0
    ):

        self.card_number = card_number
        self.customer_id = customer_id
        self.card_type = card_type
        self.expiry_date = expiry_date
        self.status = status
        self.credit_limit = credit_limit
        self.available_credit = available_credit

    def display_card(self):

        print("\n==========================================")
        print("               CARD DETAILS")
        print("==========================================")

        print("Card Number      :", self.card_number)
        print("Customer ID      :", self.customer_id)
        print("Card Type        :", self.card_type)
        print("Expiry Date      :", self.expiry_date)
        print("Status           :", self.status)

        if self.card_type == "Credit Card":

            print("Credit Limit     : ₹", self.credit_limit)
            print("Available Credit : ₹", self.available_credit)

        print("==========================================")


    def block_card(self):

        if self.status == "Blocked":

            print("\nCard is already blocked.")

        else:

            self.status = "Blocked"

            print("\nCard has been blocked successfully.")


    def activate_card(self):

        if self.status == "Active":

            print("\nCard is already active.")

        else:

            self.status = "Active"

            print("\nCard has been activated successfully.")


    def check_card_status(self):

        print("\n==========================================")
        print("             CARD STATUS")
        print("==========================================")

        print("Card Number :", self.card_number)
        print("Card Type   :", self.card_type)
        print("Status      :", self.status)

        print("==========================================")