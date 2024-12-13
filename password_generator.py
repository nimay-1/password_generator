import string
import random

# Ask for the desired password length
while True:
    try:
        password_length = int(input("Enter the desired password length: "))
        break
    except ValueError:
        print("Please enter an integer.")

# Define different options for composing the password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# List to collect the user's choices for the password composition
choices = []

# Ask if letters should be included
while True:
        include_letters = str(input("Do you want to include letters? (y/n) "))
        if include_letters == "y" or include_letters == "n":
            choices.append(include_letters)
            print("Choice has been accepted!")
            break
        else:
            print('Please enter "y" for "yes" and "n" for "no"')

# Ask if digits should be included
while True:
        include_digits = str(input("Do you want to include digits? (y/n) "))
        if include_digits == "y" or include_digits == "n":
            choices.append(include_digits)
            print("Choice has been accepted!")
            break
        else:
            print('Please enter "y" for "yes" and "n" for "no"')

# Ask if symbols should be included
while True:
        include_symbols = str(input("Do you want to include symbols? (y/n) "))
        if include_symbols == "y" or include_symbols == "n":
            choices.append(include_symbols)
            print("Choice has been accepted!")
            break
        else:
            print('Please enter "y" for "yes" and "n" for "no"')

# Error message if the user refuses to include letters, digits, and symbols
if choices == ["n", "n", "n"]:
    print("You have refused all three options. It is impossible to generate the password.")
else:
    characters = ""
    if choices[0] == "y":
        characters += letters
    if choices[1] == "y":
        characters += digits
    if choices[2] == "y":
        characters += symbols

# Generate the password by randomly selecting characters from the "characters" string, based on the length chosen by the user at the beginning
    password = "".join(random.choice(characters) for _ in range(password_length))
    print("Here is your generated password:", password)
