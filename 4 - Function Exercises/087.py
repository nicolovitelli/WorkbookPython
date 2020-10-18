""" Write a function that takes a string of characters as its first parameter, and the width of
the terminal in characters as its second parameter. Your function should return a new
string that consists of the original string and the correct number of leading spaces
so that the original string will appear centered within the provided width when it is
printed. Do not add any characters to the end of the string. Include a main program
that demonstrates your function. """
lunghezza = 80
def centro(s, lunghezza):
    if lunghezza < len(s):
        return s
    spazi = (lunghezza - len(s) // 2)
    risultato = " " * spazi + s
    return risultato

def main():
    print(centro("Questo è", lunghezza))
    print(centro("un Esempio", lunghezza))
    print(centro("Hello World", lunghezza))

if __name__ == '__main__':
    main()
