#https://adventofcode.com/2018/day/9

def slowList():                 # Will take too long for task 2
    nPlayers = 452
    lastMarble = 71250
    playerScores = dict()
    marbles = [0]
    curr = 0
    currentPlayer = 0

    for i in range(1, lastMarble+1):
        if not i % 23 == 0:
            marbles.insert((curr + 2) % len(marbles), i)
            curr = (curr + 2) % len(marbles)
        else:
            curr = (curr - 7) % len(marbles)
            popped = marbles.pop(curr)
            if not currentPlayer in playerScores.keys():
                playerScores[currentPlayer] = 0
            playerScores[currentPlayer] += i + popped
            curr = curr % len(marbles) # If popped one was last one, the right-wise to select is index-0 and len will be equal to curr
        currentPlayer = (currentPlayer + 1) % nPlayers

    print(max(playerScores.values()))



def efficientDeque(): # Leveraging deque (python's doubly-linked list), extremely more efficient
    from collections import deque
    nPlayers = 452
    lastMarble = 71250 * 100
    marbles = deque([0])
    currentPlayer = 0
    playerScores = dict()

    for i in range(1, lastMarble+1):
        if not i % 23 == 0:
            marbles.rotate(-1)
            marbles.append(i)
        else:
            marbles.rotate(7)
            popped = marbles.pop()
            if not currentPlayer in playerScores.keys():
                playerScores[currentPlayer] = 0
            playerScores[currentPlayer] += (i + popped)
            marbles.rotate(-1)
        currentPlayer = (currentPlayer + 1) % nPlayers

    print(max(playerScores.values()))
