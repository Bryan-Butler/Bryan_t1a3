import json
import os.path
from clear_terminal import clearterminal


##saves the users transactions to the users account
def save_transactions(cardholder):
    filename = "user_data.json"
    if os.path.exists(filename):
        with open(filename, "r+") as file:
            user_data = json.load(file)
            for user in user_data:
                if user["card_number"] == cardholder.get_cardnumber():
                    if "transactions" not in user:
                        user["transactions"] = []
                    user["transactions"].extend(cardholder.transactions)
                    file.seek(0)
                    file.truncate()
                    file.write(json.dumps(user_data))
                    break

#deposit to the users currently selected account
def deposit(cardholder):
    try:
        deposit_amount = float(input("How much are you depositing:\n"))
        cardholder.set_balance(cardholder.get_balance() + deposit_amount)
        cardholder.transactions.append({
            "type": "deposit",
            "amount": deposit_amount
        })
        clearterminal.clear_terminal()
        print("Your updated balance is:", "{:.2f}".format(cardholder.get_balance()))
        save_transactions(cardholder)  
    except:
        print("Invalid input, please try again")

#subtract from the users currently selected account
def withdraw(cardholder):
    try:
        withdrawal_amount = float(input("How much would you like to withdraw:\n"))
        clearterminal.clear_terminal()
        if cardholder.get_balance() < withdrawal_amount:
            print("Sorry, you are trying to withdraw more than you have.")
        else:
            cardholder.set_balance(cardholder.get_balance() - withdrawal_amount)
            cardholder.transactions.append({
                "type": "withdrawal",
                "amount": withdrawal_amount
            })
            print("Your updated balance is:", "{:.2f}".format(cardholder.get_balance()))
            save_transactions(cardholder)  
    except:
        print("Invalid input, please try again")

#check selected users account balance
def check_balance(cardholder):
    print("Your current balance is:", "{:.2f}".format(cardholder.get_balance()))

#view the selected accounts transaction history
def view_transactions(cardholder):
    print("Transaction History:")
    clearterminal.clear_terminal()
    if not cardholder.transactions:
        print("No transaction history")
    else:
        for transaction in cardholder.transactions:
            print("Type:", transaction["type"])
            print("Amount:", "{:.2f}".format(transaction["amount"]))
            print()

#calculating interest
def calculate_interest(principal, interest_rate, time_period):
    interest_rate_decimal = interest_rate / 100
    amount = principal * (1 + interest_rate_decimal) ** time_period
    interest = amount - principal
    print(f"For an interest rate of {interest_rate}% over {time_period} years:")
    print(f"Principal Amount: {principal}")
    print(f"Interest Earned: {interest:.2f}")
    print(f"Total Amount: {amount:.2f}")
    print()


#delete selected users account
def close_account(cardholder):
    print("Closing your account is an irreversible action.")
    print("Please select one of the following options:")
    print("(1) Close Account")
    print("(2) Cancel")
    choice = input("")

#check valid option selected
    while choice not in ["1", "2"]:
        print("Invalid choice. Please select again.")
        choice = input("Enter your choice: ")

 # Remove the account from the JSON file
    if choice == "1":
        entered_pin = int(input("Please enter your security pin to confirm the closure:\n"))
        if cardholder.get_cardpin() == entered_pin:
            with open("src/user_data.json", "r+") as file:
                user_data = json.load(file)
                user_data = [user for user in user_data if user["card_number"] != cardholder.get_cardnumber()]
                file.seek(0)
                file.truncate()
                file.write(json.dumps(user_data) + "\n")

            print("Account closed successfully.")
            clearterminal.clear_terminal()
        else:
            print("Invalid security pin. Account closure canceled.")
    else:
        print("Account closure canceled.")
        clearterminal.clear_terminal()
        return 


# json data loading, user creation and updating
def add_new_user(card_number, pin, first_name, last_name, balance):
    with open("user_data.json", "r") as file:
        user_data = json.load(file)

    user = {
        "card_number": card_number,
        "pin": pin,
        "first_name": first_name,
        "last_name": last_name,
        "balance": balance
    }

    user_data.append(user)

    with open("user_data.json", "w") as file:
        json.dump(user_data, file)