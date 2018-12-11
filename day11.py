#https://adventofcode.com/2018/day/11

import numpy as np

grid = np.zeros(shape=(300,300), dtype=np.int64)
serialNumber = 3463

def current(x,y):
    if x >= 300 or y >= 300:
        raise ValueError('x or y over 300')

    result = ((x + 1 + 10) * (y + 1) + serialNumber) * (x + 1 + 10)
    if len(str(result)) >= 3:
        result = str(result)[-3]
    else:
        result = str(0)
    return int(result) - 5

def sumSize(x, y, size):
    counter = 0
    breakFlag = False
    for xPlus in range(x, x + size):
        for yPlus in range(y, y + size):
            if yPlus == 300:
                break
            if xPlus == 300:
                breakFlag = True
                break
            counter += current(xPlus, yPlus)
        if breakFlag:
            break
    return counter

for x in range(300):
    for y in range(300):
        grid[x][y] = current(x,y)

# Part 1
max = [-500000, 0, 0]
for x in range(300):
    for y in range(300):
        result = sumSize(x,y,3)
        if result > max[0]:
            max = [result, x, y]

# Part 2: Not the most efficient thing ever but after 30s or so it gets stuck without new maxSized (at size == 11, tried that, worked.)
maxSized = [-500000, 0, 0, 0]
for s in range(1, 300):
    for x in range(300):
        for y in range(300):
            last = sumSize(x,y,s)
            if last > maxSized[0]:
                maxSized = [last, x, y, s]
                print(maxSized)



