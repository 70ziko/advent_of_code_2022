win = 6
draw = 3

sum = 0

with open('strategy') as strategy:
    for line in strategy:
        line = line.strip('\n')
        turn = line.split(' ')
        opponent = ord(turn[0]) - 64
        me = ord(turn[1]) - (23 + 64)
        print(opponent, ' vs ', me)
        if (me - 1 == opponent or me + 2 == opponent):
            sum += me + win
        elif (me == opponent):
            sum += me + draw
        else:
            sum += me
        print('Current points: ', sum)