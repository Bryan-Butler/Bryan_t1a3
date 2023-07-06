# Bryan Butler: Banking/ATM app


### Presentation video:
### Repository:


<br>


## Styling convention
Throughout the process of making this app, i tried to adhere to the convention's outlined in [PEP 8 - style guide for python code](https://peps.python.org/pep-0008/) as best as possible. utilising heavy use of <b> Snake_case </b> Which is a styling where the naming of things utilises an _ where their would be a space between the words.

The code is organized into logical sections and functions to improve readability and maintainability. The use of functions helps encapsulate specific tasks or operations.

Commenting used fairly thoroughly throughout to indicate what code is doing what.


<br>


## Features
I have quite a few features, some simpler than others but all interact with the JSON file storage that ive implemened. Ill talk about just a few, the login validation, the transaction history and finally how all the data is saved to the JSON file.

### Login validation
When first selecting existing user, you will be presented with two options, the first of which being existing user, once you select this you will be asked to provide your card number or your name, and it will match it against the data saved in the JSON file and subsequently check the pin (that must be digits) against the data saved their also.

![login validating](/docs/login%20validating.gif)



### Transaction history
What you can see here is passed transactions that have been stored into the JSON file, even from seperate instances of the program running showing, with both the type of transaction and how much.
![Transaction history](/docs/transaction%20history.gif)


### saving data to a JSON file



