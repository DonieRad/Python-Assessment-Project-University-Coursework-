# TASK 2

# a) Take 5 integers as input and store in a set
user_integers_list = []
for _ in range(5):
    number = int(input("Enter an integer: "))
    user_integers_list.append(number)

set1 = set(user_integers_list)
print("The set of entered integers is:", set1)


# b) Compare two sets
def compared_sets(set1, set2):
    print('Integers common to both sets:', set1 & set2)  # Intersection
    print('Integers in either or both sets:', set1 | set2)  # Union


integers_set1 = {4, 8, 14, 56, 78, 2, 48}
integers_set2 = {8, 15, 2, 48, 46, 32, 5}
compared_sets(integers_set1, integers_set2)


# c) Print a set in descending order
def descending_order(integers_set):
    integers_list = list(integers_set)
    integers_list.sort()     # Ascending
    integers_list.reverse()  # Now descending
    print(integers_list)


integers_set = {4, 5, 12, 8, 45, 1, 7, 9, 64}
descending_order(integers_set)
