""" Write a program that allows the user to convert a number from one base to another.
Your program should support bases between 2 and 16 for both the input number and
the result number. If the user chooses a base outside of this range then an appropriate
error message should be displayed and the program should exit. Divide your program
into several functions, including a function that converts from an arbitrary base to
base 10, a function that converts from base 10 to an arbitrary base, and a main
program that reads the bases and input number from the user. You may find your
solutions to Exercises 77, 78 and 98 helpful when completing this exercise. """
def binario_a_decimale(binario):
    cifra = len(binario)
    decimale = 0
    for i in range(len(binario)):
        val_decimale = (binario[i] * (2 ** cifra))
        decimale = decimale + int(val_decimale)
        cifra = cifra - 1
        print(decimale)

def decimale_a_binario(decimale):
    decimale = int(decimale)
    print("Valore Convertito in Binario:", bin(decimale))

def decimale_a_ottale(ottale):
    ottale = int(ottale)
    print("Valore Convertito in Ottale:", oct(ottale))

def decimale_a_esadecimale(esadecimale):
    esadecimale = int(esadecimale)
    print("Valore Convertito in Esadecimale:", hex(esadecimale))

def binario_a_ottale(bin2ottale):
    bin2ottale = int(bin2ottale)
    print("Valore Convertito in Ottale:", oct(bin2ottale))

def binario_a_esadecimale(bin2esa):
    bin2esa = int(bin2esa)
    print("Valore Convertito in Esadecimale:", hex(bin2esa))

def main():
    print("1: Binario a Decimale\n2: Decimale a Binario\n3: Decimale a Ottale\n4: Decimale a Esadicimale\n"
                   "5: Binario a Ottale\n6: Binario a Esadecimale")
    scelta = input("-----------> ")
    if scelta == "1":
        binario = input("Inserisci Numbero Binario: ")
        binario_a_decimale(binario)
    elif scelta == "2":
        decimale = input("Inserisci Numero Decimale: ")
        decimale_a_binario(decimale)
    elif scelta == "3":
        ottale = input("Inserisci Numero Decimale: ")
        decimale_a_ottale(ottale)
    elif scelta == "4":
        esadecimale = input("Inserisci Numero Decimale: ")
        decimale_a_esadecimale(esadecimale)
    elif scelta == "5":
        bin2ottale = input("Inserisci Numero Binario: ")
        binario_a_ottale(bin2ottale)
    elif scelta == "6":
        bin2esa = input("Inserisci Numero Binario: ")
        binario_a_esadecimale(bin2esa)
    else:
        return "Scelta Non Valida"

if __name__ == '__main__':
    main()
