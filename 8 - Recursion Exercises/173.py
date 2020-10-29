""" Run-length encoding is a simple data compression technique that can be effective when repeated values occur at
adjacent positions within a list. Compression is achieved by replacing groups of repeated values with one copy of the
value, followed by the number of times that the value should be repeated. For example, the list ["A",
"A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B",
"B", "B", "A", "A", "A", "A", "A", "A", "B"] would be compressed
as ["A", 12, "B", 4, "A", 6, "B", 1]. Decompression is performed by
replicating each value in the list the number of times indicated.
Write a recursive function that decompresses a run-length encoded list. Your
recursive function will take a run-length compressed list as its only parameter. It will
return the decompressed list as its only result. Create a main program that displays
a run-length encoded list and the result of decoding it."""
def decode(text):
    for (char, num) in re.findall(r'([a-z])([0-9]+)', text):
        yield char * int(num)

def main():
    text = input("inserisci stringa: ")
    print(''.join(decode(text)))

if __name__ == '__main__':
    main()
