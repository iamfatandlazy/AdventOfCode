#takes in a .txt file called 'expenses.txt' that is organized with one number per line
#remove new line and checks which numbers add to 2020 and returns those
#numbers multiplied together

numToSumTo = 2020
expenses = [int(lines.strip()) for lines in open('expenses.txt', 'r')]

val2 = {x*y for x in expenses for y in expenses if x!=y and x+y==numToSumTo}
print(str(val2).strip('{}'))
