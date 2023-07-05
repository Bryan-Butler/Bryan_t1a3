import json
from bank_functions import add_new_user

def test_add_new_user():
    card_number = '1111'
    pin = '2222'
    first_name = 'lebron'
    last_name = 'james'
    balance = 1000.0

    # Add the new user using the add_new_user function
    add_new_user(card_number, pin, first_name, last_name, balance)

    # Read the test user data file and check if the user is added correctly
    with open("test_user_data.json", "r") as file:
        user_data = json.load(file)

    user = user_data[0]

    # Check if the added user matches the provided user details
    assert user["card_number"] == card_number
    assert user["pin"] == pin
    assert user["first_name"] == first_name
    assert user["last_name"] == last_name
    assert user["balance"] == balance