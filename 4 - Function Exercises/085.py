""" Words like first, second and third are referred to as ordinal numbers. In this exercise,
you will write a function that takes an integer as its only parameter and returns a
string containing the appropriate English ordinal number as its only result. Your
function must handle the integers between 1 and 12 (inclusive). It should return an
empty string if a value outside of this range is provided as a parameter. Include a
main program that demonstrates your function by displaying each integer from 1 to
12 and its ordinal number. Your main program should only run when your file has
not been imported into another program. """
def converti_int_ordinale(numero):
    if numero == 1:
        return "First"
    elif numero == 2:
        return "Second"
    elif numero == 3:
        return "Third"
    elif numero == 4:
        return "Fourth"
    elif numero == 5:
        return "Fifth"
    elif numero == 6:
        return "Sixth"
    elif numero == 7:
        return "Seventh"
    elif numero == 8:
        return "Eighth"
    elif numero == 9:
        return "Ninth"
    elif numero == 10:
        return "Tenth"
    elif numero == 11:
        return "Eleventh"
    elif numero == 12:
        return "Twelfth"
    else:
        print("Valore non valido")

def main():
    numero = int(input("Inserisci il Numero: "))
    converti_int_ordinale(numero)

    elenco_numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ordinali = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth",
                "Eleventh", "Twelfth"]
    valore = 0
    while valore != len(elenco_numeri):
        print(elenco_numeri[valore], end=" ")
        print(ordinali[valore])
        valore = valore + 1

if __name__ == '__main__':
    main()
