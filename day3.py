#https://adventofcode.com/2018/day/3
import numpy as np

grid = np.zeros(shape=(1000,1000))

orig = open('/home/giuzzilla/Desktop/input').readlines()

orig = [line.strip().replace('@ ', '').replace(':', '').replace('#', '').replace('x', ' ').replace(',', ' ') for line in orig]


orig = [line.split(' ') for line in orig]

claims = 0

for element in orig:
    initialLeft = int(element[1])
    initialTop = int(element[2])
    for rowI in range(int(element[3])):
        rowIpad = rowI + initialLeft
        for columnI in range(int(element[4])):
            columnIpad = columnI + initialTop
            if(grid[rowIpad][columnIpad] == 0):
                grid[rowIpad][columnIpad] = int(element[0])
            else:
                grid[rowIpad][columnIpad] = -1


unique, counts = np.unique(grid, return_counts=True)
enum = dict(zip(unique, counts))

for element in orig:
    n = int(element[3])*int(element[4])
    if(int(element[0]) in enum.keys()):
        if(enum[int(element[0])] == n):
            print(element[0])
