import sys,os

seats = [line.strip() for line in open(os.path.join(sys.path[0], 'seats.txt'), 'r')]



def findVal(inLine,numOfRows,lowerVal,upperVal):
    size = len(inLine)
    currentMin = 0
    currentMax = numOfRows
    for i in range(size):
        sizeOfArea = currentMax-currentMin
        if inLine[i]==lowerVal:
            currentMax = currentMin + (sizeOfArea/2)
        else:
            currentMin = currentMax - (sizeOfArea/2)

    return currentMin
    
seatIDs = [int(findVal(seat[0:7],128,'F','B'))*8+int(findVal(seat[7:10],8,'L','R')) for seat in seats]

seatIDs.sort()
lastNum = seatIDs[0] -1
for num in seatIDs:
    if num!=lastNum+1:
        print('My boarding pass ID is: '+ str(num - 1))
    lastNum = num

print('Max seat ID is: '+ str(max(seatIDs)))
#testing stuff
#print(findVal(row,128,'F','B'))
#print(findVal(col,8,'L','R'))
#print(int(findVal(row,128,'F','B'))*8+int(findVal(col,8,'L','R')))