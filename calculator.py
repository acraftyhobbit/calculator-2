"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def my_reduce(function, args):
    """Takes a function and a list of arguments and cumulatively applies the function"""
    result = function(args[0], args[1])
    for i in args[2:]:
        result = function(result, i)
    return result

commands = list()
filename = "./solution/further-study/operations.txt"
with open(filename) as f:
    for row in f:
        commands.append(row.strip())

with open('results.txt', 'wt') as f:# this writes a new file and will overwrite an existing file
    for i in commands:
        result = None
        tokens = i.split(" ")
        numbers = list()
        for item in tokens[1:]:
            try:
                numbers.append(int(item))
            except ValueError:
                result =  "Please put in a number."
        if tokens[0] == "q":
            break
        elif tokens[0] == "+":
            result =  my_reduce(add, numbers)
        elif tokens[0] == "-":
            result =  my_reduce(subtract, numbers)
        elif tokens[0] == "*":
            result =  my_reduce(multiply, numbers) 
        elif tokens[0] == "/":
            result =  my_reduce(divide, numbers)
        elif tokens[0] == "square":
            result =  square(numbers[0])
        elif tokens[0] == "cube":
            result =  cube(numbers[0])
        elif tokens[0] == "pow":
            result =  my_reduce(power, numbers)
        elif tokens[0] == "mod":
            result =  my_reduce(mod, numbers)
        else:
            result =  "Please enter a valid operation"
        f.write(str(result))
        f.write('\n')
