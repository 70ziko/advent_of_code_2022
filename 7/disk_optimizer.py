def load_commands(): # returns table
    with open('commands.txt') as input:
        signal = input.readlines()
    return signal

def main():
    print(*load_commands(), sep = '\n')

if __name__ == "__main__":
    main()