elves = []
sum = 0

with open('calories.txt') as calories:
    for line in calories:
        if line == '\n':
            elves.append(sum)
            sum = 0
            continue
        sum += int(line)

max_cal = elves[0]
second_max_cal = elves[0]
third_max_cal = elves[0]

for i in elves :
    if i > max_cal :
        third_max_cal = second_max_cal
        second_max_cal = max_cal
        max_cal = i

    elif i > second_max_cal :
        third_max_cal = second_max_cal
        second_max_cal = i

    elif i > third_max_cal :
        third_max_cal = i

three_max = max_cal + second_max_cal + third_max_cal
# fattest = max(elves)
print('The fat of the three fattest elves is: %d' % three_max)