# This code is fucking shit please don't look into it too much haha

import pandas as pd

def get_nth_letters(text, n):
    nth_letters = []
    for index, letter in enumerate(text):
        if index % n == 0:
            nth_letters.append(letter)
    return nth_letters

def load_crates(): # returns pandas dataframe
    crates = []
    formatted = []

    with open('crates.txt') as input:
        crates = input.readlines()
        for line in crates:
            line = line[1:]
            formatted.append(get_nth_letters(line, 4))
        # print(*formatted, sep='\n')
        df = pd.DataFrame(formatted)
    return df

def load_procedure(): # returns table
    formatted = []
    with open('procedure.txt') as input:
        procedure = input.readlines()
        for line in procedure:
            split = line.split()
            del split[0]
            del split[1]
            del split[2]
            formatted.append(split)
    return formatted

def CrateMover9000(crates, procedure):
    
    # print(crates)

    # DataFrame to list
    crates_list = []
    for i in range(len(crates) + 1):    # The +1 is stupid and needs fixing XD 
        crates_list.append(crates[i].tolist())

    # remove spaces from 2D list
    for j in range(len(crates_list)):
        c = crates_list[j].count(' ')
        for i in range(c):
            crates_list[j].remove(' ')

    print(*crates_list, sep='\n')

    for step in procedure:
        step = [eval(i) for i in step]
        # print(step)
        rep = step[0]
        og = step[1] - 1
        dest = step[2] - 1
        if rep != 1:
            for i in range(rep):
                popped = crates_list[og].pop(0)
                crates_list[dest].insert(0, popped)
        else:
            popped = crates_list[og].pop(0)
            crates_list[dest].insert(0, popped)
    print(pd.DataFrame(crates_list))

def CrateMover9001(crates, procedure):
    
    # print(crates)

    # DataFrame to list
    crates_list = []
    for i in range(len(crates) + 1):    # The +1 is stupid and needs fixing XD
        crates_list.append(crates[i].tolist())

    # remove spaces from 2D list
    for j in range(len(crates_list)):
        c = crates_list[j].count(' ')
        for i in range(c):
            crates_list[j].remove(' ')

    print(*crates_list, sep='\n')

    for step in procedure:
        step = [eval(i) for i in step]
        # print(step)
        rep = step[0]
        og = step[1] - 1
        dest = step[2] - 1

        pack = crates_list[og][:rep]
        crates_list[og] = crates_list[og][rep:]
        crates_list[dest][0:0] = pack

    print(pd.DataFrame(crates_list))
    

def main():
    crates = load_crates()
    procedure = load_procedure()
    # print(*procedure, sep='\n')
    CrateMover9001(crates, procedure)

if __name__ == "__main__":
    main()