""" Many people do not use capital letters correctly, especially when typing on small
devices like smart phones. In this exercise, you will write a function that capitalizes
the appropriate characters in a string. A lowercase “i” should be replaced with an
uppercase “I” if it is both preceded and followed by a space. The first character in
the string should also be capitalized, as well as the first non-space character after a
“.”, “!” or “?”. For example, if the function is provided with the string “what time
do i have to be there? what’s the address?” then it should return the string “What
time do I have to be there? What’s the address?”. Include a main program that reads
a string from the user, capitalizes it using your function, and displays the result. """
def inserimento_maiuscole(stringa):
    risultato = stringa.replace(" i ", " I ")
    if len(stringa) > 0:
        risultato = risultato[0].upper() + \
            risultato[1 : len(risultato)]

    posizione = 0
    while posizione < len(stringa):
        if risultato[posizione] == "." or risultato[posizione] == "!" or risultato[posizione] == "?":
            posizione = posizione + 1
            while posizione < len(stringa) and risultato[posizione] == " ":
                posizione = posizione + 1
            if posizione < len(stringa):
                risultato = risultato[0: posizione] + \
                    risultato[posizione].upper() + \
                    risultato[posizione + 1 : len(risultato)]
        posizione = posizione + 1
    return risultato

def main():
    stringa = input("Inserisci la Stringa: ")
    inserimento_maiuscole(stringa)

if __name__ == '__main__':
    main()
