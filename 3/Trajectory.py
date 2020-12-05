import sys,os

mapIn = [line.strip() for line in open(os.path.join(sys.path[0], 'Map.txt'), 'r')]
colCount = len(mapIn)


def slope(sx,sy):
    x=0
    y=0
    treesHit = 0

    while y<=colCount:
        
        if mapIn[y%len(mapIn)][x%len(mapIn[0])]=='#':
            treesHit+=1
        
        x+=sx
        y+=sy
    
    return treesHit

print(slope(3,1))
print(slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2))