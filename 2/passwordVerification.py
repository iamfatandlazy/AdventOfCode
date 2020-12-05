#Each line gives the password policy and then the password. 
#The password policy indicates the lowest and highest number of times a given letter 
#must appear for the password to be valid. For example, 1-3 a means that the 
# password must contain a at least 1 time and at most 3 times.

#Enjoy reading these list comprehensions

#--- Part Two ---
#While it appears you validated the passwords correctly, they don't seem to be what 
# the Official Toboggan Corporate Authentication System is expecting.

#The shopkeeper suddenly realizes that he just accidentally explained the password 
# policy rules from his old job at the sled rental place down the street! 
# The Official Toboggan Corporate Policy actually works a little differently.

#Each policy actually describes two positions in the password, where 1 
# means the first character, 2 means the second character, and so on. 
# (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
# Exactly one of these positions must contain the given letter. 
# Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

import os,sys

passwordsIn = [[pswrd[0].replace('-',' ').split(' '),pswrd[1].strip(' ')] for pswrd in [line.strip().split(':') for line in open(os.path.join(sys.path[0], 'passwords.txt'), 'r')]]

validPasswordsPart1 = [validPass for validPass in passwordsIn if sum([1 for lttr in validPass[1] if lttr in validPass[0][2]]) >= int(validPass[0][0]) and sum([1 for lttr in validPass[1] if lttr in validPass[0][2]]) <= int(validPass[0][1])]

validPasswordsPart2 = [validPass for validPass in passwordsIn if ((validPass[1][int(validPass[0][0])-1]==validPass[0][2]) ^ (validPass[1][int(validPass[0][1])-1]==validPass[0][2]))]

print(len(validPasswordsPart1))
print(len(validPasswordsPart2))
