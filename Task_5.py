# TASK 5
# Advanced input validation for character and number

while True:
    my_char = input("Please enter a single letter: ")

    if my_char.isnumeric():
        print("The character entered was numeric.")
        continue

    if len(my_char) > 1:
        print("Multiple letters entered. Taking the first letter.")
        my_char = my_char[0]

    if len(my_char) == 1 and my_char.isalpha():
        break
    else:
        print("The value entered was not a single letter. Please try again.")

while True:
    my_num = input("Please enter a number: ")

    if my_num.isnumeric():
        my_num = int(my_num)
        break
    else:
        print("The value entered was not a number. Please try again.")

print(my_char * my_num)
