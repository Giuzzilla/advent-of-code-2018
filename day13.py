#https://adventofcode.com/2018/day/13
# Very ugly version (see day13vec.py in the same repository)

input = open('/home/giuzzilla/Desktop/input').readlines()
input = [list(x.strip('\n')) for x in input]
carts = []

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


for x in range(len(input)):
    for y in range(len(input[0])):
        elem = input[x][y]
        if(elem == '^'):
            input[x][y] = '|'
            carts.append(['^', x, y, 0])
        elif(elem == '<'):
            input[x][y] = '-'
            carts.append(['<', x, y, 0])
        elif(elem == 'v'):
            input[x][y] = '|'
            carts.append(['v', x, y, 0])
        elif(elem == '>'):
            input[x][y] = '-'
            carts.append(['>', x, y, 0])

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
        sign = carts[i][0]
        currPos = input[x][y]
        if currPos == '+':
            if sign == '>':
                if turn == 0:
                    carts[i] = ['^', x - 1, y, 1]
                elif turn == 1:
                    carts[i] = ['>', x, y + 1, 2]
                elif turn == 2:
                    carts[i] = ['v', x + 1, y, 0]
            elif sign == '^':
                if turn == 0:
                    carts[i] = ['<', x, y - 1, 1]
                elif turn == 1:
                    carts[i] = ['^', x - 1, y, 2]
                elif turn == 2:
                    carts[i] = ['>', x, y + 1, 0]
            elif sign == '<':
                if turn == 0:
                    carts[i] = ['v', x + 1, y, 1]
                elif turn == 1:
                    carts[i] = ['<', x, y - 1, 2]
                elif turn == 2:
                    carts[i] = ['^', x - 1, y, 0]
            elif sign == 'v':
                if turn == 0:
                    carts[i] = ['>', x, y + 1, 1]
                elif turn == 1:
                    carts[i] = ['v', x + 1, y, 2]
                elif turn == 2:
                    carts[i] = ['<', x, y - 1, 0]
        elif currPos == '\\':
            if sign == '>':
                carts[i] = ['v', x + 1, y, turn]
            elif sign == '^':
                carts[i] = ['<', x, y - 1, turn]
            elif sign == 'v':
                carts[i] = ['>', x, y + 1, turn]
            elif sign == '<':
                carts[i] = ['^', x - 1, y, turn]
        elif currPos == '/':
            if sign == '<':
                carts[i] = ['v', x + 1, y, turn]
            elif sign == '^':
                carts[i] = ['>', x, y + 1, turn]
            elif sign == 'v':
                carts[i] = ['<', x, y - 1, turn]
            elif sign == '>':
                carts[i] = ['^', x - 1, y, turn]
        elif currPos == '-':
            if sign == '<':
                carts[i] = [sign, x, y - 1, turn]
            elif sign == '>':
                carts[i] = [sign, x, y + 1, turn]
        elif currPos == '|':
            if sign == '^':
                carts[i] = [sign, x - 1, y, turn]
            elif sign == 'v':
                carts[i] = [sign, x + 1, y, turn]

        collisions = checkCollisions(carts)

        if collisions:
            if not firstCollided:  # Part 1
                firstCollided = collisions[0]
                print("Part 1: " + str(firstCollided[3]) + ',' + str(firstCollided[2]))

            for collision in collisions:
                toDelete.add(collision[0])
                toDelete.add(collision[1])

