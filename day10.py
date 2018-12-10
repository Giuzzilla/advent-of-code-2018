#https://adventofcode.com/2018/day/10
# Initially tried to plot on matplotlib but it's not necessary (it works tho)
#import numpy as np
#import matplotlib.pyplot as plt

input = open('/home/giuzzilla/Desktop/input').readlines()
input = [x.strip().replace('position=<', '').replace(',', '').replace('velocity=<','').replace('>','').split(' ') for x in input]

points = []

for line in input:
    temp = []
    for elem in line:
        if elem != '':
            temp.append(int(elem))
    points.append(temp)

secs = 15000 #try for a decent amount of times, you have to reach the global minima, which is found for a secs big enough

minSize = 100
final_i = 0
for i in range(secs):
    currentPoints = []
    for point in points:
        currentPoints.append([point[0] + i*point[2],point[1] + i*point[3]])
    minX = min(currentPoints, key=lambda l: l[0])[0]
    maxX = max(currentPoints, key=lambda l: l[0])[0]
    minY = min(currentPoints, key=lambda l: l[1])[1]
    maxY = max(currentPoints, key=lambda l: l[1])[1]
    size = (maxX - minX) + (maxY - minY)
    if size < minSize:
        minSize = size
        final_i = i



resultPoints = []

for point in points:
    resultPoints.append([point[0]+final_i*point[2], point[1]+final_i*point[3]])

minX = min(resultPoints, key=lambda l: l[0])[0]
maxX = max(resultPoints, key=lambda l: l[0])[0]
minY = min(resultPoints, key=lambda l: l[1])[1]
maxY = max(resultPoints, key=lambda l: l[1])[1]

for y in range(minY, maxY+1):
    line = ''
    for x in range(minX, maxX+1):
        if([x,y] in resultPoints):
            line += '*'
        else:
            line += ' '
    print(line)