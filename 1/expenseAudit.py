#takes in a .txt file called 'expenses.txt' that is organized with one number per line
#remove new line and checks which numbers add to 2020 and returns those
#numbers multiplied together
import os
import sys

numToSumTo = 2020
expenses = [int(lines.strip()) for lines in open(os.path.join(sys.path[0], 'expenses.txt'), 'r')]

def twoValues():
    return {x*y for x in expenses for y in expenses if x+y==numToSumTo}

def threeValues():
    return {x*y*z for x in expenses for y in expenses for z in expenses if x+y+z==numToSumTo}

print(str(threeValues()).strip('{}'))
