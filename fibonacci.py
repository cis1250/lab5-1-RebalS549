#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def validating_user_input():
    while True:
        user_input = input("How many terms of the Fibonacci sequence do you want? ")

        # Validate input
        if not user_input.isdigit() or int(user_input) <= 0:
            print("Please enter a positive integer.")
            continue
            
        return int(user_input)

def fibonacci_sequence(user_input):
    n = int(user_input)
    sequence = []  # create an empty list to store numbers
    a, b = 0, 1

    for i in range(n):
        sequence.append(a)  # add the current number to the list
        a, b = b, a + b

    return sequence

def print_sequence():
    n = validating_user_input()
    fib_list = fibonacci_sequence(n)
    print(f"The Fibonacci sequence with {n} terms is: {fib_list}")


# Run the program
print_sequence()
