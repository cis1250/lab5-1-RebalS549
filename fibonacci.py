#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def fibonacci_sequence():
    while True:
        user_input = input("How many terms of the Fibonacci sequence do you want? ")

        # Validate input
        if not user_input.isdigit() or int(user_input) <= 0:
            print("Please enter a positive integer.")
            continue

        n = int(user_input)
        # Generate Fibonacci sequence
        a, b = 0, 1
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()  # new line after sequence
        break
