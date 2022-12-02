lose_x = 0
draw_y = 3
win_z = 6

sum = 0

with open('strategy') as strategy:
    for line in strategy:
        line = line.strip('\n')
        turn = line.split(' ')
        opponent = ord(turn[0]) - 65
        outcome = (ord(turn[1]) - (23 + 65)) * 3
        print(opponent + 1, ' with outcome ', outcome)

        if (outcome == 6):
            me = (opponent + 1) % 3
            print('My move: ', me + 1)
            sum += outcome + me + 1
        elif (outcome == 3):
            me = opponent
            print('My move: ', me + 1)
            sum += outcome + me + 1
        elif (outcome == 0):
            me = (opponent + 2) % 3
            print('My move: ', me + 1)
            sum += outcome + me + 1
        
print('Sum of points: ', sum)
        # if (me - 1 == opponent or me + 2 == opponent):
        #     sum += me + win
        # elif (me == opponent):
        #     sum += me + draw
        # else:
        #     sum += me

        # print('Current points: ', sum)