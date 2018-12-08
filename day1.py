#https://adventofcode.com/2018/day/1

orig = open('/home/giuzzilla/Desktop/input').readlines()

orig = [int(item.strip()) for item in orig]

print(sum(orig)) # Print sum (task 1)

previous = set([0])  #Initially used a list, set() is faster because O(1) (instead of O(n)) average lookup
i = 0 
counter = 0
while(True):
    counter += orig[i%len(orig)]
    if(counter in previous):
        print(counter)
        break  #Stop at second encounter of same frequency (task 2)
    previous.add(counter)
    i += 1


