def find_common(str0, str1, str2):
    for c in str0:
        for d in str1:
            if c == d:
                for e in str2:
                    if c == e:
                        common = c
    return common

def count_value(c):
    value = ord(c)
    if value >= 97 and value <= 122:
        value -= 96
    elif value >= 65 and value <= 90:
        value = value + 26 - 64
    return value

def load(): # return 2d list with groups
    group = []
    groups = []
    with open('rucksack_input.txt') as input:
        sacks = input.readlines()

        for id, line in enumerate(sacks):
            line = line.strip('\n')
            group.append(line)
            if len(group) >= 3:
                groups.append(group)
                group = []

    return groups

def main():
    sum = 0
    groups = load()
    
    for group in groups:
        common = find_common(group[0], group[1], group[2])
        sum += count_value(common)
        print(group, '\n', common, '\nCurrent sum:',sum)

if __name__ == "__main__":
    main()