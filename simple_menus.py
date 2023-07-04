#logged in menu
def print_menu():
    print("Please choose an option from the following")
    print("(1) Deposit")
    print("(2) Withdraw")
    print("(3) Show Balance")
    print("(4) View Transaction History")
    print("(5) Calculate interest")
    print("(6) Close Account")
    print("(7) Exit")

#user type menu
def user_selection_menu():
    print("Are you a:")
    print("(1) Existing user")
    print("(2) New user")


#enter to continue
def enter_continue():
    input("Press Enter to continue...")

#return menu
def return_user_select():
    print("Returning to user selection.")

#enter initial details
def enter_details():
    print("Please enter your card number, first name or type 'return' to go back:")
    user_input = input("")
    return user_input
    
#no matching user
def no_matching_user():
    print("No matching user found. Please try again.")

#generic invalid input
def invalid_input():
    print("Invalid input, please try again")

#pin does not match
def pin_not_match():
    print("The pin you provided does not match our records.")

#invalid choice
def invalid_choice():
    print("Invalid choice. Please select again.")

#ask for security pin
def security_pin():
    return input("Please enter your security pin:\n").strip()

#input had letters/characters and not just numbers
def invalid_pin_input():
    print("Error: Invalid input. Please enter only digits for the pin.")
