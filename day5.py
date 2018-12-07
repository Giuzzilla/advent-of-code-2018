#https://adventofcode.com/2018/day/5
import sys
input = open('/home/giuzzilla/Desktop/input').read()

input = input.strip()

lower = list('abcdefghijklmnopqrstuvwxyz')
upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

list1 = [x[0] + x[1] for x in zip(lower,upper)]
list2 = [x[0] + x[1] for x in zip(upper,lower)]
list1.extend(list2)

sys.setrecursionlimit(10000)

def replacing(toReplace, listComb):      # Keep replacing combinations found inside the string (recursively)
    for elem in listComb:
        originLen = len(toReplace)
        toReplace = toReplace.replace(elem, '')
        afterLen = len(toReplace)
        if originLen != afterLen:
            toReplace = replacing(toReplace, listComb)
    return toReplace 

final = replacing(input[:], list1)

print(len(final)) 

#2nd part

finalList = []
for i in range(len(lower)):
    cleanedStr = input[:].replace(lower[i], '').replace(upper[i], '')
    finalList.append([lower[i], len(replacing(cleanedStr[:], list1))])

finalList.sort(key= lambda x: x[1])
print(finalList)
print(len(finalList))
