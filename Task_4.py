# TASK 4
# Ask user for a single letter and check uppercase/lowercase

my_char = input("Please enter a single letter: ")

if len(my_char) != 1:
    print("The value entered was not a single letter.")
else:
    if my_char.isupper():
        print("An uppercase letter has been entered.")
    else:
        print("A lowercase letter has been entered.")
