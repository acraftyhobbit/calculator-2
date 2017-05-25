"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


while True:
    math_calculation = raw_input(">")
    tokens = math_calculation.split(" ")
    numbers = list()
    for item in tokens[1:]:
        try:
            numbers.append(int(item))
        except ValueError:
            print "Please put in a number."
    if tokens[0] == "q":
        break
    elif tokens[0] == "+":
        print reduce(add, numbers)
    elif tokens[0] == "-":
        print reduce(subtract, numbers)
    elif tokens[0] == "*":
        print reduce(multiply, numbers) 
    elif tokens[0] == "/":
        print reduce(divide, numbers)
    elif tokens[0] == "square":
        print square(numbers[0])
    elif tokens[0] == "cube":
        print cube(numbers[0])
    elif tokens[0] == "pow":
        print reduce(power, numbers)
    elif tokens[0] == "mod":
        print reduce(divide, mod)
    else:
        print "Please enter a valid operation"
