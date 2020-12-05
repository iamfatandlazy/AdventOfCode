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
validPassports2 = [passport.split(' ') for passport in formattedData]
for passport in validPassports2:
    del passport[0]

for passport in validPassports2:
    for item in passport:
        if 'byr' in item:
            byr = item[4:len(item)-1]
            if int(byr) < 1920 and int(byr) >2002:
                validPassports2.remove(passport)
                break


        if 'iyr' in item:
            iyr = item[4:len(item)-1]
            if int(iyr) < 2010 and int(iyr) > 2020:
                validPassports2.remove(passport)
                break


        if 'eyr' in item:
            eyr = item[4:len(item)-1]
            if int(eyr) < 2020 and int(eyr) > 2030:
                validPassports2.remove(passport)
                break


        if 'hgt' in item:
            unit = item[len(item)-2:len(item)-1]
            hgt = item[4:len(item)-3]
            if unit=='cm':
                if int(hgt)<150 and int(hgt)>193:
                    validPassports2.remove(passport)
                    break
            elif unit=='in':
                if int(hgt)<59 and int(hgt)>76:
                    validPassports2.remove(passport)
                    break
        

        if 'hcl' in item:
            hex = ['0123456789abcdef']
            hcl = item[4:len(item)-1]
            if hcl[0]!='#':
                validPassports2.remove(passport)
                break
            elif len(item[5:len(item)-1])!=6 and not item[5:len(item)-1] in hex:
                validPassports2.remove(passport)
                break


        if 'ecl' in item:
            ecl = item[4:len(item)-1]
            if ecl not in eyeColor:
                validPassports2.remove(passport)
                break


        if 'pid' in item:
            pid = item[4:len(item)-1]
            if len(pid)!=9 and item.isnumeric:
                validPassports2.remove(passport)
                break

            
        
print((validPassports2))
#print(len(validPassports1))