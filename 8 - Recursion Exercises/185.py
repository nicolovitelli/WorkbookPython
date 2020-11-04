""" Write a recursive function that decompresses a run-length encoded list. Your recursive function will take a run-length
 compressed list as its only argument. It will return the decompressed list as its only result. Create a main program
 that displays a run-length encoded list and the result of decoding it. """
def decode(text):
    for (char, num) in re.findall(r'([a-z])([0-9]+)', text):
        yield char * int(num)

def main():
    print(''.join(decode('a10b2c3')))

if __name__ == '__main__':
    main()
