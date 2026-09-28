class Customer:

    def __init__(self, customer_id, name, phone, email, address, pin):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.pin = pin

    def display_customer(self):
        print("\n========== CUSTOMER DETAILS ==========")
        print("Customer ID :", self.customer_id)
        print("Name        :", self.name)
        print("Phone       :", self.phone)
        print("Email       :", self.email)
        print("Address     :", self.address)
        print("======================================")