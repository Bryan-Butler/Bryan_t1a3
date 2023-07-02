import json
from cardinfo import card_info
from clear_terminal import clear_terminal


def print_menu():
    print("Please choose an option from the following using the corresponding number")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")


def deposit(cardholder):
    try:
        deposit_amount = float(input("How much are you depositing:\n"))
        cardholder.set_balance(cardholder.get_balance() + deposit_amount)
        print("Your updated balance is:", str(cardholder.get_balance()))
    except:
        print("Invalid input, please try again")


def withdraw(cardholder):
    try:
        withdrawal_amount = float(input("How much would you like to withdraw:\n"))
        if cardholder.get_balance() < withdrawal_amount:
            print("Sorry, you are trying to withdraw more than you have.")
        else:
            cardholder.set_balance(cardholder.get_balance() - withdrawal_amount)
    except:
        print("Invalid input, please try again")


def check_balance(cardholder):
    print("Your current balance is:", cardholder.get_balance())


if __name__ == "__main__":
    current_user = card_info("","","","","")

    while True:
        print("Are you a:")
        print("1. Existing user")
        print("2. New user")
        user_choice = input("")

        if user_choice == "1":
            while True:
                search_input = input("Please enter your card number or name, or type 'return' to go back:\n")
                if search_input.lower() == "return":
                    print("Returning to user selection.")
                    break

                with open("user_data.json", "r") as file:
                    user_data = json.load(file)
                    user_matches = [holder for holder in user_data if
                                    holder["card_number"] == search_input or
                                    holder["first_name"] == search_input or
                                    holder["last_name"] == search_input]

                if len(user_matches) > 0:
                    current_user_data = user_matches[0]
                    current_user = card_info(current_user_data["card_number"], current_user_data["pin"],
                                             current_user_data["first_name"], current_user_data["last_name"],
                                             current_user_data["balance"])
                    break
                else:
                    print("No matching user found. Please try again.")

            if search_input.lower() == "return":
                continue

            while True:
                user_pin = int(input("Please enter your security pin:\n").strip())
                if current_user.get_cardpin() == user_pin:
                    break
                else:
                    print("Invalid pin, please try again.")

        elif user_choice == "2":
            card_number = input("Please enter your card number, or type 'return' to go back:\n")
            if card_number.lower() == "return":
                print("Returning to user selection.")
                continue
            
            pin = int(input("Please enter your security pin:\n"))
            first_name = input("Please enter your first name:\n")
            last_name = input("Please enter your last name:\n")
            balance = float(input("Please enter your initial balance:\n"))

            current_user = card_info(card_number, pin, first_name, last_name, balance)
            print("New user created successfully.")

            # Save the new user's data to the JSON file
            with open("user_data.json", "a") as file:
                user_data = {
                    "card_number": card_number,
                    "pin": pin,
                    "first_name": first_name,
                    "last_name": last_name,
                    "balance": balance
                }
                file.write(json.dumps(user_data) + "\n")

        elif user_choice.lower() == "return":
            print("Returning to initial screen.")
            continue

        print("Welcome", current_user.get_firstname())
        option = 0
        while True:
            print_menu()
            try:
                option = int(input())
            except:
                print("Invalid input, please try again")

            if option == 1:
                deposit(current_user)
            elif option == 2:
                withdraw(current_user)
            elif option == 3:
                check_balance(current_user)
            elif option == 4:
                break
            else:
                option = 0

        print("Thank you for using our services!")
        break
