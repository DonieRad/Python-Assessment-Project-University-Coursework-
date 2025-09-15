# TASK 3
# Reading numbers from file, calculating average, and finding smallest even

import os

filename = "numbers2.txt"

if not os.path.exists(filename):
    print(f"Error: '{filename}' not found. Please make sure it exists in the same folder.")
else:
    try:
        # a) Read first line of file
        with open(filename, 'r') as file:
            line = file.readline()
            print("First line:", line.strip())

        # b) Read full file into a list of integers
        with open(filename, 'r') as file:
            numbers = file.readlines()

        my_numbers = []
        for line in numbers:
            # Split line by spaces and convert to integers
            my_numbers.extend([int(num) for num in line.split()])

        my_numbers.sort()
        print('These are numbers in my_numbers list:', my_numbers)

        # c) Calculate average
        if my_numbers:
            numbers_average = sum(my_numbers) / len(my_numbers)
            print('The average of my_numbers is:', numbers_average)
        else:
            print("No numbers found in the file.")

        # d) Find smallest even number
        even_numbers = [num for num in my_numbers if num % 2 == 0]
        if even_numbers:
            smallest_even_number = min(even_numbers)
            print('The smallest even number is:', smallest_even_number)
        else:
            print("There are no even numbers in the list.")

    except ValueError:
        print("Error: The file contains non-numeric data. Please check the file contents.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
