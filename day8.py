#https://adventofcode.com/2018/day/8

input = open('/home/giuzzilla/Desktop/input').read().split(" ")

input = [int(x) for x in input]

def explore(nNodes, subList):
    sumMetaData = 0
    totalLen = 0
    nSubNodes = []
    nMetadata = []
    for j in range(nNodes):
        nSubNodes.append(subList[totalLen])
        nMetadata.append(subList[totalLen + 1])
        if(nSubNodes[j] == 0):
            sumMetaData += sum(subList[totalLen + 2: totalLen + 2 + nMetadata[j]])
            totalLen += 2 + nMetadata[j]
        else:
            totalLen += 2
            result = explore(nSubNodes[j], subList[totalLen:])
            totalLen += result[0]
            sumMetaData += result[1]
            sumMetaData += sum(subList[totalLen : totalLen + nMetadata[j]])
            totalLen += nMetadata[j]

    return [totalLen, sumMetaData]

print("1st Solution: " + str(explore(1, input)[1]))

def explore2(nNodes, subList):
    sumMetaData = []
    totalLen = 0
    nSubNodes = []
    nMetadata = []
    for j in range(nNodes):
        nSubNodes.append(subList[totalLen])
        nMetadata.append(subList[totalLen + 1])
        if(nSubNodes[j] == 0):
            sumMetaData.append(sum(subList[totalLen + 2: totalLen + 2 + nMetadata[j]]))
            totalLen += 2 + nMetadata[j]
        else:
            totalLen += 2
            result = explore2(nSubNodes[j], subList[totalLen:])
            totalLen += result[0]
            counter = 0
            for elem in subList[totalLen : totalLen + nMetadata[j]]:
                if elem - 1 < len(result[1]):
                    counter += result[1][elem - 1]
            sumMetaData.append(counter)
            totalLen += nMetadata[j]

    return [totalLen, sumMetaData]

print("2nd Solution: " + str(explore2(1, input)[1][0]))