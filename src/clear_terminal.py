import os

#Clears the terminal screen.
class clearterminal:
    def clear_terminal():    
        os.system('cls' if os.name == 'nt' else 'clear')