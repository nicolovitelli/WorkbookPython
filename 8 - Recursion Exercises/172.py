""" Another game that some people play with the names of chemical elements involves
constructing a sequence of elements where each element in the sequence begins with
the last letter of its predecessor. For example, if a sequence begins with Hydrogen,
then the next element must be an element that begins with N, such as Nickel. The
element following Nickel must begin with L, such as Lithium. The element sequence
that is constructed can not contain any duplicates.
Write a program that reads the name of an element from the user. Your program
should use a recursive function to find the longest sequence of elements that begins
with the entered element. Then it should display the sequence. Ensure that your
program responds in a reasonable way if the user does not enter a valid element name. """
elements_fname = "../Data/Elements.csv"
def longestSequence(start, words):
    if start == "":
        return []
    best = []
    last_letter = start[len(start) - 1].lower()
    for i in range(0, len(words)):
        first_letter = words[i][0].lower()
        if first_letter == last_letter:
            candidate = longestSequence(words[i], words[0 : i] + words[i + 1 : len(words)])
            if len(candidate) > len(best):
                best = candidate
    return  [start] + best

def loadNames():
    names = []
    inf = open(elements_fname, "r")
    for line in inf:
        line = line.rstrip()
        parts = line.split(",")
        names.append(parts[2])
    inf.close()
    return names

def main():
    names = loadNames()
    start = input("inserisci nome elemnto")
    start = start.capitalize()
    names.remove(start)
    sequence = longestSequence(start, names)
    print("la sequenza piu lunga che inizia con", start, "è")
    for element in sequence:
        print(" ", element)
    
if __name__ == '__main__':
    main()
