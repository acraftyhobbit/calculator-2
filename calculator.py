"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    math_calculation = raw_input(">")
    tokens = math_calculation.split(" ")
    #if the first token is "q":
    #    quit
    if tokens[0] == "q":
        break
    elif tokens[0] == "+":
        results = add(int(tokens[1]), int(tokens[2]))
        print results
    elif tokens[0] == "-":
        results = subtract(int(tokens[1]), int(tokens[2]))
        print results
    elif tokens[0] == "*":
        results = multiply(int(tokens[1]), int(tokens[2]))
        print results
    elif tokens[0] == "/":
        print divide(float(tokens[1]), float(tokens[2]))
    elif tokens[0] == "square":
        print square(int(tokens[1]))
    elif tokens[0] == "cube":
        print cube(int(tokens[1]))
    elif tokens[0] == "pow":
        print power(int(tokens[1]), int(tokens[2]))
    elif tokens[0] == "mod":
        print mod(int(tokens[1]), int(tokens[2]))