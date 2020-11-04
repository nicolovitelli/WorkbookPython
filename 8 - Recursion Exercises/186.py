""" Write a recursive function that implements the run-lenght compression technique described in Exercise 185. Your
function will take a list or a string as its only arugment. It should return the run-length compressed list as its
only result. Include a main program that reads a string form the user, compresses it, and displays the run-length
encoded result. """
def encode(data):
    if len(data) == 0:
        return []
    index = 1
    while index < len(data) and data[index] == data[index - 1]:
        index = index + 1
    current = [data[0], index]
    return current + encode(data[index : len(data)])

def main():
    s = input("inserisci qualche carattere: ")
    print(encode(s))

if __name__ == '__main__':
    main()
