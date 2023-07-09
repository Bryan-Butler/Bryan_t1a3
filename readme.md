# Bryan Butler: Banking/ATM app



###  [Github](https://github.com/Pepperz/Bryan_t1a3)
###  [Youtube](https://youtu.be/CvidepagsE0)


<br>


## Coding conventions
Throughout the process of making this app, i tried to adhere to the convention's outlined in pep as best as possible. utilising heavy use of <b> Snake_case </b> Which is a styling where the naming of things utilises an _ where their would be a space between the words.

The code is organized into logical sections and functions to improve readability and maintainability. The use of functions helps encapsulate specific tasks or operations.

Commenting used fairly thoroughly throughout to indicate what code is doing what.


<br>

## Help Documentation

This program was developed in python 3.10.6, please ensure you have the following installed:

<b>python 3.10.6 or newer:</b> [python.org](https://www.python.org/downloads/)

<b> bash:</b> [Windows](https://hackernoon.com/how-to-install-bash-on-windows-10-lqb73yj3) or [Mac](https://scriptingosx.com/2019/02/install-bash-5-on-macos/)

<b> pip:</b>[pypi.org/pip](https://pypi.org/project/pip/)

<br>

## System Requirements

This application will run on any modern windows or mac machine. No intense hardware requirements.

</br>

## How to install and run

1. Down the "sec" folder in its entirety from the Github repository.

2. Open a terminal and navigate to the "src" folder in the terminal, this will be wherever you saved the download to i.e "user/download".

3. Once here, type ls -la and we will see all the files.

![ls -la](/docs/ls%20-la%20example.png)

4. Type into the terminal ./script.sh to run the app. <b> If you get a permissions error type chmod +x ./script.sh and then repeat step 4. </b>

5. Repeat these steps to run run_test.sh also.

<br>

## List of Features

### Login validation
When first selecting existing user, you will be presented with two options, the first of which being existing user, once you select this you will be asked to provide your card number or your name, and it will match it against the data saved in the JSON file and subsequently check the pin (that must be digits) against the data saved their also.

![login validating](/docs/login%20validating.gif)

<br>

### Creating a new user

![Create new user](/docs/create%20new%20user.gif)

<br>

### Deposit and withdraw

![Deposit nd withdraw](/docs/deposit%20and%20withdraw.gif)

<br>

### Show balance and transaction history
What you can see here is passed transactions that have been stored into the JSON file, even from seperate instances of the program running showing, with both the type of transaction and how much.

![Transaction history](/docs/show%20balance%20and%20transaction%20history.gif)

<br>

### Interest calculator

![Interest Calculator](/docs/Interest%20calculator.gif)

<br>

### Close account

![Close account](./docs/Close%20account.gif)

<br>


### How to use the app

#### Start screen
The start screen will ask you to pick from options 1-3

![start screen](/docs/Start%20screen.png)


- Inputting "1" means you are an existing user and ask for your card number or name to match against the database.
- Inputting "2" will take you to account creation and will generate you a 16 digit card number then ask you to set a pin and your name.
- inputting "3" here exits the app.

#### Main menu

The main menu has 7 options.

![Main menu](/docs/Main%20menu.png)


- Inputting "1" will take you to a deposit menu, asking you how much youd like to deposit.
- Inputting "2", similarly will take you to a withdrawal menu, asking you much youd like to withdrawal.
- Inputting "3" will show your current balance.
- Inputting "4" will let you see your past transactions associated with your account.
- Inputting "5" will take you to an intereste calculator, asking for term length, interest rate etc similar to what we see on bank websites today.
- Inputting "6" will begin the process of closing your account and deleting it from the database, having you confirm your pin before doing so.
- Inputting "7" will take you back to the start screen.

## Development 

#### First steps

Initial steps were to create a board using [Trello](trello.com) to help keep on track and prioritise what steps to do next, and possible add things as development went along.

![Trello](/docs/trello%201.png)

| Task     | Deadline | Status | 
| -------------- | ------- |------- |
| Create git Repo  | 2/7/23  | Done | 
| Connect git | 2/7/23 | Done |
| Create Trello Board | 2/27/23 | Done |
| Write pseudocode | 2/7/23 | Done |
| Create initial python files | 2/7/23 | Done |

<br>

#### JSON data storage
| Task     | Deadline | Status | 
| -------------- | ------- |------- |
| Create json file  | 3/7/23  | Done | 
| Create and impliment function to load/read json on app start| 3/7/23 | Done |
| Create and impliment function to save/update data to json | 3/27/23 | Done |
| Create and impliment function to retrieve data from json | 3/7/23 | Done |
| Test json functions| 3/7/23 | Done |

#### Matching existing user
![trello](docs/trello%202.png)
| Task     | Deadline | Status | 
| -------------- | ------- |-------|
| Create promopt for info from user  | 3/7/23  | Done | 
| Create functions to match info to json info| 3/7/23 | Done |
| Create logged in menu | 3/27/23 | Done |
| Create function to load user's transaction history | 3/7/23 | Done |
| Test | 3/7/23 | Done |

#### Deleteing/Closing account

| Task     | Deadline | Status | 
| -------------- | ------- |------- |
| Create interface for closing menu | 5/7/23  | Done | 
| Validate they are the user with pin match | 5/7/23 | Done |
| Create function to delete users info | 5/27/23 | Done |
| test | 5/7/23 | Done |

#### Create executeables

![trello](docs/trello%203.png)
| Task     | Deadline | Status | 
| -------------- | ------- |------- |
| Create shell script files| 6/7/23  | Done | 
| Identify dependencies/requirements| 6/27/23 | Done |
| Write launch script | 6/7/23 | Done |
| Test Script in dev environment| 6/27/23 | Done |
