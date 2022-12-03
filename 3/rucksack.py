def find_common(str0, str1):
    for c in str0:
        for d in str1:
            if c == d:
                common = d
    return common

def count_value(c):
    value = ord(c)
    if value >= 97 and value <= 122:
        value -= 96
    elif value >= 65 and value <= 90:
        value = value + 26 - 64
    return value

def main():
    sum = 0

    with open('rucksack_input.txt') as input:
        for line in input:
            first_half = line[0:len(line)//2]
            sec_half = line[len(line)//2:]

            print(line, first_half, ' | ', sec_half, end = '')
            common = find_common(first_half, sec_half)
            print(common, "Value:", count_value(common))
            sum += count_value(common)
            print(sum, '\n')


if __name__ == "__main__":
    main()