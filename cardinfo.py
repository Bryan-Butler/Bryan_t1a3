class card_info():
    def __init__(self, cardnumber, cardpin, firstname, lastname, balance):
        self.cardnumber = cardnumber
        self.pin = cardpin
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    
    ##getting the info.
    def get_cardnumber(self):
        return self.cardnumber
    def get_cardpin(self):
        return self.pin
    def get_firstname(self):
        return self.firstname
    def get_lastname(self):
        return self.lastname
    def get_balance(self):
        return self.balance
    
    ###setting the info
    def set_cardnumber(self, new_val):
        self.cardnumber = new_val
    def set_cardpin(self, new_val):
        self.cardpin = new_val
    def set_firstname(self,new_val):
        self.firstname = new_val
    def set_lastname(self, new_val):
        self.lastname = new_val
    def set_balance(self, new_val):
        self.balance = new_val

    def print_out(self):
        print("Card #: ", self.cardnumber)
        print("Your pin is: ", self.cardpin)
        print("First name: ", self.firstname)
        print("Last name: ", self.lastname)
        print("Balance: ", self.balance)
