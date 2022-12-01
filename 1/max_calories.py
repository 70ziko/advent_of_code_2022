elves = []
sum = 0

with open('calories.txt') as calories:
    for line in calories:
        if line == '\n':
            elves.append(sum)
            sum = 0
            continue
        sum += int(line)
            
fattest = max(elves)
print('The fat of the fattest elv is: %d' % fattest)