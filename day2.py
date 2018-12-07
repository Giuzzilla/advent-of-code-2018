#https://adventofcode.com/2018/day/2

orig = open('/home/giuzzilla/Desktop/input').readlines()
orig = [item.strip() for item in orig]

count2 = 0
count3 = 0

for item in orig:
    counted2 = False
    counted3 = False
    unique_letters = set(item)
    for letter in unique_letters:
        innerCount = item.count(letter)
        if innerCount == 2 and not counted2:
            count2 += 1
            counted2 = True
        if innerCount == 3 and not counted3:
            count3 += 1
            counted3 = True
        if counted2 and counted3:
            break

print(count2*count3)

#2nd part 

for i in range(len(orig)):
    for j in range(len(orig) - (i+1)):
        counterSimilar = 0
        for k in range(len(orig[i])):
            if orig[i][k] == orig[j + i][k]:
                counterSimilar += 1
        if counterSimilar == len(orig[i]) - 1:
            print(orig[i] + "\n" + orig[j + i])
            break

#2nd part (2nd method w/ Hamming distance)

from itertools import combinations
def hamming2(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

for x in combinations(orig, 2):
    if(hamming2(x[0],x[1]) == 1):
        print(x[0]+"\n"+x[1])
