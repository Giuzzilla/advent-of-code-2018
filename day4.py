#https://adventofcode.com/2018/day/4
orig = open('/home/giuzzilla/Desktop/input').readlines()


orig = [item[1:].strip().replace('-', '').replace(' ', '', 1).replace(':', '').split('] ') for item in orig]

orig.sort(key = lambda item: item[0])

sleepTimes = dict()

for event in orig:
    if('Guard' in event[1]):
        guardId = int(event[1].split(" ")[1].strip("#"))
        continue
    if('falls' in event[1]):
        startSleep = int(event[0][-2:])
        continue
    if('wakes' in event[1]):
        endSleep = int(event[0][-2:])
        if(guardId not in sleepTimes.keys()):
            sleepTimes[guardId] = [endSleep - startSleep]
            sleepTimes[guardId].append([startSleep])
            sleepTimes[guardId].append([endSleep])
        else:
            sleepTimes[guardId][0] += endSleep - startSleep
            sleepTimes[guardId][1].append(startSleep)
            sleepTimes[guardId][2].append(endSleep)


#2nd part

mostSleptOfAll = [0,0,0]

for key in sleepTimes.keys():
    sleptMinutes = [0]*60

    start = sleepTimes[key][1]
    end = sleepTimes[key][2]

    for i in range(60):
        for j in range(len(start)):
            if i < end[j] and i >= start[j]:
                sleptMinutes[i] += 1
    
    if(max(sleptMinutes) > mostSleptOfAll[2]):
        mostSleptOfAll[0] = key
        mostSleptOfAll[1] = sleptMinutes.index(max(sleptMinutes))
        mostSleptOfAll[2] = max(sleptMinutes)
        

print(mostSleptOfAll)
