import sys,os,re

requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
eyeColor = ['amb','blu','brn','gry','grn','hzl','oth']

data = [line.strip() for line in open(os.path.join(sys.path[0], 'PassengerData.txt'), 'r')]
formattedData = ['']

index = 0
for i in data:
    if i != '':
        formattedData[index] += ' ' + i
    else:
        formattedData.append('')
        index+=1

#part 1
validPassports1 = formattedData

for field in requiredFields:
    for passport in validPassports1:
        if field not in passport:
            validPassports1.remove(passport)


#part 2
#ACTUALLY handling the data and making it into a key value pair to easily use
validPassports2 = [passport.split(' ') for passport in formattedData]
validPassportDict = []
for passport in validPassports2:
    del passport[0]
    passportDict = {}
    for item in passport:
        (key,val) = item.split(':')
        passportDict[key] = val
    validPassportDict.append(passportDict)
    
for passport in validPassportDict:
    for key in passport:
        if key=='byr':
            if int(passport[key])<1920 or int(passport[key])>2002:
                validPassportDict.remove(passport)
                break
        
        elif key=='iyr':
            if int(passport[key])<2010 or int(passport[key])>2020:
                validPassportDict.remove(passport)
                break

        elif key=='eyr':
            if int(passport[key])<2020 or int(passport[key])>2030:
                validPassportDict.remove(passport)
                break

        elif key=='hgt':
            unit = passport[key][len(passport[key])-2:len(passport[key])]
            if unit.lower()==('cm'):
                num = int(passport[key][0:len(passport[key])-2])
                if num<150 or num>193:
                    validPassportDict.remove(passport)
                    break

            elif unit.lower()==('in'):
                num = int(passport[key][0:len(passport[key])-2])
                if num<59 or num>76:
                    validPassportDict.remove(passport)
                    break
        
        elif key=='hcl':
            if len(passport[key])==7 and passport[key][0]=='#':
                for char in passport[key][1:len(passport[key])]:
                    if char not in('0123456789abcdef'):
                        validPassportDict.remove(passport)
                        break
            else:
                validPassportDict.remove(passport)
                break


            





#print((validPassports2))
print(validPassportDict)
#print(len(validPassports1))