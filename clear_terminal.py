import os

#Clears the terminal screen.

def clear_terminal():    
    os.system('cls' if os.name == 'nt' else 'clear')
