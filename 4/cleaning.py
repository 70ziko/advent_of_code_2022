def check_pairs(groups):
    c = 0
    for pair in groups:
        a = pair[0].split('-')
        b = pair[1].split('-')
        a = [eval(i) for i in a]
        b = [eval(i) for i in b]

        if a[0] >= b[0] and a[1] <= b[1]:
            c += 1
            print('contains:', pair)
        elif b[0] >= a[0] and b[1] <= a[1]:
            c += 1
            print('contains:', pair)
        else:
            print('not:', pair)
    return c

def check_pairs_overlap(groups):
    c = 0
    for pair in groups:
        a = pair[0].split('-')
        b = pair[1].split('-')
        a = [eval(i) for i in a]
        b = [eval(i) for i in b]

        if a[0] >= b[0] and a[0] <= b[1]:
            c += 1
            print('contains:', pair)
        elif b[0] >= a[0] and b[0] <= a[1]:
            c += 1
            print('contains:', pair)
        elif a[1] >= b[0] and a[1] <= b[1]:
            c += 1
            print('contains:', pair)
        elif b[1] >= a[0] and b[1] <= a[1]:
            c += 1
            print('contains:', pair)
        else:
            print('not:', pair)
    return c

def load(): # return 2d list with groups
    pair = []
    groups = []
    with open('section_pairs.txt') as input:
        for line in input:
            line = line.strip('\n')
            pair = line.split(',')
            groups.append(pair)
    return groups

def main():
    groups = load()
    pairs_contain = check_pairs(groups)
    pairs_overlap = check_pairs_overlap(groups)
    print('Par które się zawierają: ', pairs_contain, 
        '\nPar, które się nakładają: ', pairs_overlap)

if __name__ == "__main__":
    main()