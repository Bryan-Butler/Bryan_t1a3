import json
from cardinfo import card_info

#load user data from JSON file
def load_user_data():
    with open("user_data.json", "r") as file:
        user_data = json.load(file)
    return user_data

#save user data to JSON file
def save_user_data(user_data):
    with open("user_data.json", "w") as file:
        json.dump(user_data, file, indent=4)

# Test case 1: Existing user with correct pin
def test_existing_user_correct_pin():
    user_data = load_user_data()
    user = user_data[0]  

    search_input = user["card_number"]
    user_pin = user["pin"]

    current_user_data = [user]
    current_user = card_info(user["card_number"], user["pin"], user["first_name"], user["last_name"], user["balance"])
    assert current_user.get_cardpin() == user_pin

    if "transactions" in current_user_data:
        current_user.transactions = current_user_data["transactions"]

    assert current_user.get_cardnumber() == user["card_number"]
    assert current_user.get_firstname() == user["first_name"]
    assert current_user.get_lastname() == user["last_name"]
    assert current_user.get_balance() == user["balance"]



# Test case 2: Existing user with incorrect pin
def test_existing_user_incorrect_pin():
    user_data = load_user_data()
    user = user_data[0]  

    search_input = user["card_number"]
    user_pin = "0000"  # Incorrect pin

    current_user_data = [user]
    current_user = card_info(user["card_number"], user["pin"], user["first_name"], user["last_name"], user["balance"])
    assert current_user.get_cardpin() != user_pin


# Test case 3: Non-existing user
def test_non_existing_user():
    user_data = load_user_data()

    search_input = "1234567890123456"

    user_matches = [holder for holder in user_data if holder["card_number"] == search_input or
                    holder["first_name"].lower() == search_input.lower() or
                    holder["last_name"].lower() == search_input.lower()]
    assert len(user_matches) == 0


# Run the test cases
test_existing_user_correct_pin()
test_existing_user_incorrect_pin()
test_non_existing_user()
