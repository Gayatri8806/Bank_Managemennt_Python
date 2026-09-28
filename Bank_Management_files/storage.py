import json
import os


# Location of bank_data.json
DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "bank_data.json"
)


# -----------------------------------------
# Create default data structure
# -----------------------------------------
def create_empty_data():

    return {
        "customers": [],
        "accounts": [],
        "loans": [],
        "cards": [],
        "transactions": [],
        "complaints": []
    }


# -----------------------------------------
# Load data from JSON file
# -----------------------------------------
def load_data():

    try:

        # Create data folder if it does not exist
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

        # Create JSON file if it does not exist
        if not os.path.exists(DATA_FILE):

            data = create_empty_data()

            with open(DATA_FILE, "w") as file:
                json.dump(data, file, indent=4)

            return data

        # Read existing data
        with open(DATA_FILE, "r") as file:

            data = json.load(file)

        # Make sure all required sections exist
        default_data = create_empty_data()

        for key in default_data:

            if key not in data:
                data[key] = []

        return data

    except json.JSONDecodeError:

        print("\nBank data file is corrupted.")
        print("Creating a new empty data structure.")

        return create_empty_data()

    except Exception as e:

        print("\nError while loading bank data:", e)

        return create_empty_data()


# -----------------------------------------
# Save data into JSON file
# -----------------------------------------
def save_data(data):

    try:

        # Make sure data folder exists
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

        with open(DATA_FILE, "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )

        print("\nBank data saved successfully.")

    except Exception as e:

        print("\nError while saving bank data:", e)