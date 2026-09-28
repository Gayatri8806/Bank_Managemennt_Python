import re


# -----------------------------------------
# Validate Customer ID
# -----------------------------------------
def validate_customer_id(customer_id):

    if not customer_id:
        return False

    if len(customer_id) < 2:
        return False

    return True


# -----------------------------------------
# Validate Name
# -----------------------------------------
def validate_name(name):

    if not name:
        return False

    if not name.replace(" ", "").isalpha():
        return False

    return True


# -----------------------------------------
# Validate Phone Number
# -----------------------------------------
def validate_phone(phone):

    if not phone.isdigit():
        return False

    if len(phone) != 10:
        return False

    return True


# -----------------------------------------
# Validate Email
# -----------------------------------------
def validate_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if re.match(pattern, email):
        return True

    return False


# -----------------------------------------
# Validate 4-digit PIN
# -----------------------------------------
def validate_pin(pin):

    if len(pin) != 4:
        return False

    if not pin.isdigit():
        return False

    return True


# -----------------------------------------
# Validate Amount
# -----------------------------------------
def validate_amount(amount):

    try:

        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except ValueError:

        return False


# -----------------------------------------
# Validate Positive Integer
# -----------------------------------------
def validate_positive_integer(value):

    try:

        value = int(value)

        if value <= 0:
            return False

        return True

    except ValueError:

        return False


# -----------------------------------------
# Validate Account Number
# -----------------------------------------
def validate_account_number(account_number):

    if not account_number:
        return False

    if not account_number.startswith("ACC"):
        return False

    return True


# -----------------------------------------
# Validate Loan Amount
# -----------------------------------------
def validate_loan_amount(amount, minimum, maximum):

    try:

        amount = float(amount)

        if amount < minimum:
            return False

        if amount > maximum:
            return False

        return True

    except ValueError:

        return False