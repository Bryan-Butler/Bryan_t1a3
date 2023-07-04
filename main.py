import json
import random
import os
from cardinfo import card_info
from clear_terminal import clearterminal
from simple_menus import (print_menu, user_selection_menu,enter_continue,
                          return_user_select,invalid_choice,security_pin,
                          invalid_pin_input,invalid_input,no_matching_user,
                          pin_not_match,enter_details)
from bank_functions import (deposit, withdraw, check_balance,view_transactions, calculate_interest, close_account)


# Create the user_data.json file if it doesn't exist
if not os.path.isfile("user_data.json"):
    with open("user_data.json", "w") as file:
        file.write("[]")

if __name__ == "__main__":
    clearterminal.clear_terminal()
    current_user = card_info("", "", "", "", "")

    while True:
        user_selection_menu()
        user_choice = input("")
        clearterminal.clear_terminal()

        while user_choice not in ["1", "2"]:
            invalid_choice()
            user_selection_menu()
            user_choice = input("")
            clearterminal.clear_terminal()

        if user_choice == "1":
            while True:
                search_input = enter_details()
                clearterminal.clear_terminal()

                if search_input == "return":
                    return_user_select()
                    break

                with open("user_data.json", "r") as file:
                    user_data = json.load(file)
                    user_matches = [holder for holder in user_data if
                                    holder["card_number"] == search_input or
                                    holder["first_name"].lower() == search_input.lower() or
                                    holder["last_name"].lower() == search_input.lower()]

                if len(user_matches) > 0:
                    current_user_data = user_matches[0]
                    current_user = card_info(current_user_data["card_number"],
                                            current_user_data["pin"],
                                            current_user_data["first_name"],
                                            current_user_data["last_name"],
                                            current_user_data["balance"])

                    user_pin = security_pin()
                    clearterminal.clear_terminal()

                    if not user_pin.isdigit() or current_user.get_cardpin() != int(user_pin):
                        if not user_pin.isdigit():
                            invalid_pin_input()
                        else:
                            pin_not_match()

                        enter_continue()
                        clearterminal.clear_terminal()
                        continue

                    # Load transaction history from JSON file
                    if "transactions" in current_user_data:
                        current_user.transactions = current_user_data["transactions"]

                    break

                else:
                    no_matching_user()
                    enter_continue()
                    clearterminal.clear_terminal()

            if search_input == "return":
                continue
        elif user_choice == "2":
            while True:
                while True:
                    card_number = ""
                    for _ in range(16):
                        digit = str(random.randint(0, 9))
                        card_number += digit

                    if len(card_number) == 16:
                        break

                print("Generated card number:", card_number)

                if card_number == "return":
                    return_user_select
                    break

                while True:
                    pin = security_pin()
                    clearterminal.clear_terminal()

                    if not pin.isdigit():
                        invalid_pin_input()
                        enter_continue()
                        clearterminal.clear_terminal()
                        continue

                    pin = int(pin)
                    break

                first_name = input("Please enter your first name:\n").lower()
                clearterminal.clear_terminal()
                last_name = input("Please enter your last name:\n").lower()
                clearterminal.clear_terminal()
                balance = float(input("Please enter your initial balance:\n"))
                clearterminal.clear_terminal()

                current_user = card_info(
                    card_number, pin, first_name, last_name, balance)
                print("New user created successfully.")

                # Load existing user data from the JSON file
                with open("user_data.json", "r") as file:
                    user_data = json.load(file)

                # Create a new user data dictionary
                user_data_entry = {
                    "card_number": card_number,
                    "pin": pin,
                    "first_name": first_name,
                    "last_name": last_name,
                    "balance": balance
                }

                # Add the new user data to the list, and save to the json file.
                user_data.append(user_data_entry)
                with open("user_data.json", "w") as file:
                    json.dump(user_data, file, indent=4)
                break

        clearterminal.clear_terminal()
        print("Welcome", current_user.get_firstname())

        while True:
            for i in range(1, 8):
                clearterminal.clear_terminal()
                print_menu()
                option = input()
                clearterminal.clear_terminal()

                try:
                    option = int(option)
                    if option == 1:
                        deposit(current_user)
                        enter_continue()
                    elif option == 2:
                        while True:
                            withdraw(current_user)
                            enter_continue()
                            break
                    elif option == 3:
                        while True:
                            check_balance(current_user)
                            enter_continue()
                            break
                    elif option == 4:
                        while True:
                            view_transactions(current_user)
                            enter_continue()
                            break
                    elif option == 5:
                        principal = float(
                            input("Enter the principal amount: "))
                        interest_rate_percent = float(
                            input("Enter the interest rate (in percentage): "))
                        interest_rate = interest_rate_percent
                        time_period = int(
                            input("Enter the time period (in years): "))
                        calculate_interest(
                            principal, interest_rate, time_period)
                        enter_continue()
                    elif option == 6:
                        close_account(current_user)
                        current_user = card_info("", "", "", "", "")
                        break
                    elif option == 7:
                        break
                    else:
                        raise ValueError()
                except ValueError:
                    invalid_input
                    enter_continue()
                    clearterminal.clear_terminal()
                    continue

            if option == 7:
                print("Thank you for using our services!")
                print("Have a great day!")
                enter_continue()
                break
            
        clearterminal.clear_terminal()