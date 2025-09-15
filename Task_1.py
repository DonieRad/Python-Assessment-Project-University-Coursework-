# TASK 1
# a) Function that filters numbers greater than 5 from a list using list comprehension

def foo(a):
    # Creates a new list (b) with numbers from (a) greater than 5
    b = [j for j in a if j > 5]
    print(b)


# b) Function rewritten using a while loop
def foo_while_loop(a):
    b = []   # Empty list to add valid numbers
    i = 0    # Index for iteration

    # While loop to iterate through the list
    while i < len(a):
        if a[i] > 5:          # Check if number > 5
            b.append(a[i])    # Add it to list b
        i += 1

    print(b)


# Example runs
foo([1, 4, 6, 9, 3, 7])
foo_while_loop([1, 4, 6, 9, 3, 7])
