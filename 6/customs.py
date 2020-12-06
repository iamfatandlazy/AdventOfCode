import os,sys

lines = [line.strip() for line in open(os.path.join(sys.path[0], 'input.txt'), 'r')]

uniqueData = []
individualAnwsers = []

tmpStrng = ''
tmpList = []

for item in lines:
    if item!='':
        tmpStrng = tmpStrng + item
        tmpList.append(item)
    else:
        uniqueData.append(''.join(set(tmpStrng)))
        individualAnwsers.append(tmpList)
        tmpList = []
        tmpStrng = ''

part1Output = uniqueData.copy()

for i in range(len(individualAnwsers)):
    for answer in individualAnwsers[i]:
        for char in uniqueData[i]:
            if char not in answer:
                uniqueData[i] = uniqueData[i].replace(char,'')

print(sum([len(entry) for entry in part1Output]))
print(sum([len(entry) for entry in uniqueData]))
#print(individualAnwsers)
#print(str(len(uniqueData))+','+str(len(individualAnwsers)))
#print(formattedData)
