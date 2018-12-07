#https://adventofcode.com/2018/day/6
#import numpy as np
input = open('/home/giuzzilla/Desktop/input').readlines()


input = [x.strip().split(', ') for x in input]
input = [[int(x[0]),int(x[1])] for x in input]

maxX = max(input, key=lambda r: r[0])[0]
maxY = max(input, key=lambda r: r[1])[1]
#grid = np.full((maxX, maxY), '.') Not necessary

notToCount = set()

#for i in range(len(input)):
#    grid[input[i][0]-1][input[i][1]-1] = str(i)

counts = dict()
notToCount = set()

def ManDist(x1, x2, y1, y2):    #Helper to make the code more readable
    return abs(x1-x2) + abs(y1-y2)


counter = 0 #2nd part
def distanceFromAll(i,j):
    dist = 0    
    for elem in input:
        dist += ManDist(i, elem[0], j, elem[1])
    return dist

for i in range(maxX-1):
    for j in range(maxY-1):
        dist = 0
        minDistPoint = min(input, key=lambda c: ManDist(i, c[0], j, c[1]))
        minDist = ManDist(i, minDistPoint[0], j, minDistPoint[1])
        ind = []
        n = 0
        for k in input:
            if ManDist(i, k[0], j, k[1]) == minDist:
                ind.append(n)
            n += 1
        
        if(distanceFromAll(i,j) < 10000):   #2nd part
            counter += 1

        if(len(ind) != 1):
            continue
        
        currValue = str(ind[0])
      
        if(i == 0 or j == 0 or i == (maxX-1) or j == (maxY-1)):
            notToCount.add(currValue)
        
        if(currValue in notToCount):
            continue
        
        if currValue not in counts.keys():
            counts[currValue] = 1
        else:
            counts[currValue] += 1


maximum_finite = max(counts.items(), key=lambda item: item[1])
print(counts)
print("1st solution: " + maximum_finite)

#grid2 = np.full((maxX, maxY), '.')
#Print 2nd part counter
print("2nd solution: " + counter)

