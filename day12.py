#https://adventofcode.com/2018/day/12

from matplotlib import pyplot as plt

input = open('/home/giuzzilla/Desktop/input').readlines()

input = [x.strip() for x in input]

iS = list(input[0].split(": ")[1])
rules = input[2:]
rules = dict([(x.split(" ")[0], x.split(" ")[2]) for x in rules])


generations = 1000
zero = 0
plotX = []
plotY = []

print(iS)
for gen in range(1, generations + 1):
    while iS[-4:] != ['.']*4:
        iS.append('.')

    iS = iS[::-1]

    while iS[-4:] != ['.']*4:
        iS.append('.')
        zero += 1

    iS = iS[::-1]

    newGen = iS[:]
    counter = 0
    for i in range(2, len(newGen) - 3):
        current = ''.join(iS[i-2:i+3])
        if current in rules:
            newGen[i] = rules[current]
        else:
            newGen[i] = '.'
        if (iS[i] == '#'):
            counter += (i - zero)
    print(str(gen) + "°: " + str(counter))
    plotX.append(gen)
    plotY.append(counter)
    iS = newGen
    newGen = []


plt.plot(plotX, plotY)   # 50 billions is a bit too much, let's try to find some regularities
plt.show()

# It stabilises after a certain number of generations, with a constant derivative (straight line).
# By looking at the graph it seems that well before 200 it was already stabilised
# So let's compute the derivative at 200 < x < 1000

deriv = (plotY[999] - plotY[200]) / (len(plotY) - 1 - 200)

# It's 32 for my input, this can also be seen by seeing the differences in values across the last generations

# So let's extrapolate only for the last

print(plotY[-1] + deriv*(50000000000 - len(plotY) + 1))





