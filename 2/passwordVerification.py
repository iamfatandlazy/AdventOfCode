#Each line gives the password policy and then the password. 
#The password policy indicates the lowest and highest number of times a given letter 
#must appear for the password to be valid. For example, 1-3 a means that the 
# password must contain a at least 1 time and at most 3 times.

#Enjoy reading these list comprehensions

import os,sys

passwordsIn = [[pswrd[0].replace('-',' ').split(' '),pswrd[1].strip(' ')] for pswrd in [line.strip().split(':') for line in open(os.path.join(sys.path[0], 'passwords.txt'), 'r')]]

validPasswords = [validPass for validPass in passwordsIn if sum([1 for lttr in validPass[1] if lttr in validPass[0][2]]) >= int(validPass[0][0]) and sum([1 for lttr in validPass[1] if lttr in validPass[0][2]]) <= int(validPass[0][1])]


print(len(validPasswords))