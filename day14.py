#https://adventofcode.com/2018/day/14

input = 330121
input2 = [int(digit) for digit in str(input)]

recipes = [3, 7]
i1 = 0
i2 = 1

while True:
    nextNumber = recipes[i1] + recipes[i2]
    if nextNumber >= 10:
        firstToAdd = nextNumber//10
        secondToAdd = nextNumber - firstToAdd*10
        recipes.append(firstToAdd)
        if recipes[-len(input2):] == input2:
            break
        recipes.append(secondToAdd)
        if recipes[-len(input2):] == input2:
            break
    else:
        recipes.append(nextNumber)
        if recipes[-len(input2):] == input2:
            break
    i1 = (i1 + 1 + recipes[i1])%len(recipes)
    i2 = (i2 + 1 + recipes[i2])%len(recipes)

recipes = [str(x) for x in recipes]
result1 = ''.join(recipes[input:input+10])
input2 = [str(item) for item in input2]
result2 = str(len(recipes[:''.join(recipes).index(''.join(input2))]))


print("Part 1: " + result1)
print("Part 2: " + result2)
