#https://adventofcode.com/2018/day/7

input = open('/home/giuzzilla/Desktop/input').readlines()
input = [x.strip().split(" ") for x in input]
input = [[x[1], x[-3]] for x in input]

graph = dict() 

fullList = set()

for pair in input:
    fullList.add(pair[0])
    fullList.add(pair[1])
    
fullList = sorted(fullList)

for elem in fullList:
    graph[elem] = []

for pair in input:
    graph[pair[0]].append(pair[1])
    graph[pair[0]] = sorted(graph[pair[0]])

dependencies = dict()

for elem in fullList:
    dependencies[elem] = []
    for arr in graph.items():
        if elem in arr[1]:
            dependencies[elem].append(arr[0])
    dependencies[elem] = sorted(dependencies[elem])

finished1 = [] # final list for first problem
finished2 = [] # final list for second problem
finishedTimed = [] # absolute time for every letter
working = [] # letters with work currently being done 
clock = 0 # absolute clock
stepTimes = dict() # remaining times for letters
nWorkers = 5 # Number of elves doing the work

for step in fullList:  # Fill dict of stepTimes with total times for every letter
    stepTimes[step] = 60 + fullList.index(step) + 1    

def isAvailable(step, final): # Check if "step" has its dependencies met thanks to the list "final"
    for dep in dependencies[step]:
        if dep not in final:
            return False
    return True

def availableList(final): # List the steps which have their dependencies met in "final"
    l = []    
    for step in fullList:
        if step not in final and isAvailable(step, final) and step not in working:
            l.append(step)
    return sorted(l)

while(True): # Cycle through available list (sorted alphabetically, note the return of the function) and insert only the first
    if(len(availableList(finished1)) == 0):
        break
    finished1.append(availableList(finished1)[0])

    
while(True):
    clock += 1
    working.extend(availableList(finished2)[:nWorkers-len(working)])
    print("Queue :" + str(availableList(finished2)))
    print("Time " + str(clock) + ": " + str(list(map(lambda l: [l, stepTimes[l]], working))))

    
    if(len(working) == 0):
        break

    for i in range(nWorkers):
        try:
            stepTimes[working[i]] -= 1
            if(stepTimes[working[i]] == 0):
                finished2.append(working[i])
                finishedTimed.append([working[i], clock])
        except IndexError: 
            continue

    for i in range(nWorkers):
        try:
            if(stepTimes[working[i]] == 0):
                del working[i]
        except IndexError: 
            continue


print("1st solution: " + ''.join(finished1))
finishedTimed.sort(key=lambda l: l[1])
print("2nd string (not solution): " + ''.join(list(map(lambda l: l[0], finishedTimed))))
print("2nd solution: " + str(clock - 1))
