from models.customer import Customer
from utils.storage import load_data, save_data


class CustomerService:

    def __init__(self):
        self.data = load_data()

    # -----------------------------------------
    # Add customer
    # -----------------------------------------
    def add_customer(self):

        print("\n==========================================")
        print("             ADD CUSTOMER")
        print("==========================================")

        customer_id = input("Enter Customer ID: ").strip()

        # Check duplicate customer
        for customer in self.data["customers"]:

            if customer["customer_id"] == customer_id:

                print("\nCustomer already exists.")
                return

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

        save_data(self.data)

        print("\n==========================================")
        print("       CUSTOMER ADDED SUCCESSFULLY")
        print("==========================================")
        print("Customer ID :", customer_id)
        print("Name        :", name)
        print("Phone       :", phone)
        print("Email       :", email)
        print("==========================================")


    # -----------------------------------------
    # View customer
    # -----------------------------------------
    def view_customer(self):

        print("\n==========================================")
        print("            CUSTOMER DETAILS")
        print("==========================================")

        customer_id = input("Enter Customer ID: ").strip()

        for customer_data in self.data["customers"]:

            if customer_data["customer_id"] == customer_id:

                customer = Customer(
                    customer_data["customer_id"],
                    customer_data["name"],
                    customer_data["phone"],
                    customer_data["email"],
                    customer_data["address"],
                    customer_data["pin"]
                )

                customer.display_customer()
                return

        print("\nCustomer not found.")


    # -----------------------------------------
    # View all customers
    # -----------------------------------------
    def view_all_customers(self):

        print("\n==========================================")
        print("             ALL CUSTOMERS")
        print("==========================================")

        if len(self.data["customers"]) == 0:

            print("\nNo customers found.")
            return

        for customer_data in self.data["customers"]:

            customer = Customer(
                customer_data["customer_id"],
                customer_data["name"],
                customer_data["phone"],
                customer_data["email"],
                customer_data["address"],
                customer_data["pin"]
            )

            customer.display_customer()