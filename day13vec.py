#https://adventofcode.com/2018/day/13
#This is an improvement of my original code, with the carts represented as R^2 vectors
from math import cos, sin, pi

input = open('/home/giuzzilla/Desktop/input').readlines()
input = [list(x.strip('\n')) for x in input]
carts = []

def rotate(vector, angle):   # Function to rotate the vectors on intersections
    x = vector[0]*int(cos(angle)) - vector[1]*int(sin(angle))
    y = vector[0]*int(sin(angle)) + vector[1]*int(cos(angle))
    return [x, y]

def checkCollisions(listCarts):
    collisions = []
    for i in range(len(listCarts)):
        for j in range(i + 1, len(listCarts)):
            if carts[i][1] == carts[j][1] and carts[i][2] == carts[j][2]:
                collisions.append([i, j, carts[i][1], carts[i][2]])
    if collisions:
        return collisions
    else:
        return False

for x in range(len(input)):   # Remove from the inputs the carts, and add them in a separate array
    for y in range(len(input[0])):
        elem = input[x][y]
        if(elem == '^'):
            input[x][y] = '|'
            carts.append([[-1, 0], x, y, 0])
        elif(elem == '<'):
            input[x][y] = '-'
            carts.append([[0, -1], x, y, 0])
        elif(elem == 'v'):
            input[x][y] = '|'
            carts.append([[1, 0], x, y, 0])
        elif(elem == '>'):
            input[x][y] = '-'
            carts.append([[0, 1], x, y, 0])

toDelete = set()
firstCollided = []
while True:
    if len(toDelete) > 0:
        toDelete = sorted(toDelete)
        for i in range(len(toDelete)):
            del carts[toDelete[i] - i]
        toDelete = set()
    if (len(carts) == 1):
        print("Part 2: " + str(carts[0][2]) + ',' + str(carts[0][1]))  # Part 2
        break
    carts = sorted(carts, key=lambda x: (x[1], x[2]))
    for i in range(len(carts)):
        x = carts[i][1]
        y = carts[i][2]
        turn = carts[i][3]
        vector = carts[i][0]
        currPos = input[x][y]
        if currPos == '+':
            if turn == 0:
                vector = rotate(vector, pi/2)
            elif turn == 2:
                vector = rotate(vector, -pi/2)
            turn = (turn + 1) % 3
        elif currPos == '\\':
            if vector[0] == 0:
                vector = rotate(vector, -pi/2)
            else:
                vector = rotate(vector, pi/2)
        elif currPos == '/':
            if vector[0] == 0:
                vector = rotate(vector, pi / 2)
            else:
                vector = rotate(vector, -pi / 2)

        carts[i] = [vector, x + vector[0], y + vector[1], turn]
        collisions = checkCollisions(carts)

        if collisions:
            if not firstCollided:  # Part 1
                firstCollided = collisions[0]
                print("Part 1: " + str(firstCollided[3]) + ',' + str(firstCollided[2]))

            for collision in collisions:
                toDelete.add(collision[0])
                toDelete.add(collision[1])

