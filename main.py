import json
from cardinfo import card_info
from clear_terminal import clearterminal
from bank_functions import (print_menu, save_transactions, deposit, withdraw, check_balance, view_transactions, close_account)

if __name__ == "__main__":
    clearterminal.clear_terminal()

    current_user = card_info("", "", "", "", "")

    while True:
        print("Are you a:")
        print("(1) Existing user")
        print("(2) New user")
        user_choice = input("")

        while user_choice not in ["1", "2"]:
            clearterminal.clear_terminal()
            print("Invalid choice. Please select again.")
            print("Are you a:")
            print("(1) Existing user")
            print("(2) New user")
            user_choice = input("")

        if user_choice == "1":
            while True:
                clearterminal.clear_terminal()
                search_input = input("Please enter your card number or name, or type 'return' to go back:\n").lower()
                if search_input == "return":
                    print("Returning to user selection.")
                    break

                with open("user_data.json", "r") as file:
                    user_data = json.load(file)
                    user_matches = [holder for holder in user_data if
                                    holder["card_number"] == search_input or
                                    holder["first_name"].lower() == search_input or
                                    holder["last_name"].lower() == search_input]

                if len(user_matches) > 0:
                    current_user_data = user_matches[0]
                    current_user = card_info(current_user_data["card_number"],
                                             current_user_data["pin"],
                                             current_user_data["first_name"],
                                             current_user_data["last_name"],
                                             current_user_data["balance"])
                    break
                
                else:
                    print("No matching user found. Please try again.")

            if search_input == "return":
                continue

            while True:
                clearterminal.clear_terminal()

                user_pin = int(input("Please enter your security pin:\n").strip())
                if current_user.get_cardpin() == user_pin:
                    break
                else:
                    print("Invalid pin, please try again.")

        elif user_choice == "2":
            while True:
                clearterminal.clear_terminal()
                card_number = input("Please enter your card number, or type 'return' to go back:\n").lower()
                if card_number == "return":
                    print("Returning to user selection.")
                    break

                pin = int(input("Please enter your security pin:\n"))
                first_name = input("Please enter your first name:\n").lower()
                last_name = input("Please enter your last name:\n").lower()
                balance = float(input("Please enter your initial balance:\n"))

                current_user = card_info(card_number, pin, first_name, last_name, balance)
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

                # Add the new user data to the list
                user_data.append(user_data_entry)

                # Save the updated user data to the JSON file
                with open("user_data.json", "w") as file:
                    json.dump(user_data, file, indent=4)


                break

        clearterminal.clear_terminal()

        print("Welcome", current_user.get_firstname())

        while True:
            print_menu()
            try:
                option = int(input())
            except:
                print("Invalid input, please try again")

            if option == 1:
                clearterminal.clear_terminal()
                deposit(current_user)
            elif option == 2:
                clearterminal.clear_terminal()
                withdraw(current_user)
            elif option == 3:
                clearterminal.clear_terminal()
                check_balance(current_user)
            elif option == 4:
                clearterminal.clear_terminal()
                view_transactions(current_user)
            elif option == 5:
                clearterminal.clear_terminal()
                close_account(current_user)
                break
            elif option == 6:
                break
            else:
                option = 0

        if option == 6:
            clearterminal.clear_terminal()
            break

    print("Thank you for using our services!")
    print("Have a great day!")