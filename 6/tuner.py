def load_signal(): # returns table
    with open('signal.txt') as input:
        signal = input.readline()
    return signal

def find_marker(signal):
    signal_len = len(signal)
    rest = signal_len % 4
    for i in range(signal_len - rest):
        
        buffer = [signal[i + x] for x in range(4)]
        if len(set(buffer)) == len(buffer):
            return i + 4

def find_message(signal):
    signal_len = len(signal)
    rest = signal_len % 4
    for i in range(signal_len - rest):
        
        buffer = [signal[i + x] for x in range(14)]
        if len(set(buffer)) == len(buffer):
            return i + 14

def main():
    signal = load_signal()
    print(find_message(signal))
    

if __name__ == "__main__":
    main()