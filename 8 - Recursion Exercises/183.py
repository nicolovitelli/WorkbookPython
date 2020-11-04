""" Write a program that reads the name of an element from the user and uses a recursive function to find the
longest sequence of elements that begins with that value. Display the sequence once it has been computed. Ensure that 
your program responds in a reasonable way if the user does not enter a valid element name. """
ELEMENTS_FNAME = "../Data/Elements.csv"
def longestSequence(start, words):
    if start == "":
        return []
    best = []
    last_letter = start[len(start) - 1].lower()
    for i in range(0, len(words)):
        first_letter = words[i][0].lower()
        if first_letter == last_letter:
            candidate = longestSequence(words(i), words[0 : i] + words[i + 1 : len(words)])
            if len(candidate) > len(best):
                best = candidate
    return  [start] + best

def loadNames():
    names = []
    inf = open(ELEMENTS_FNAME, "r")
    for line in inf:
        line = line.rstrip()
        parts = line.split(",")
        names.append(parts[2])
    inf.close()
    return names

def main():
    names = loadNames()
    start = input("inserisci nome di un elemento: ")
    start = start.capitalize()
    if start in names:
        names.remove(start)
        sequence = longestSequence(start, names)
        for element in sequence:
            print("", element)
    else:
        print("non valido")

if __name__ == '__main__':
    main()
