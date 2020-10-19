import math

""" Write a function that takes two positive integers that represent the numerator and
denominator of a fraction as its only two parameters. The body of the function
should reduce the fraction to lowest terms and then return both the numerator and
denominator of the reduced fraction as its result. For example, if the parameters
passed to the function are 6 and 63 then the function should return 2 and 21. Include
a main program that allows the user to enter a numerator and denominator. Then
your program should display the reduced fraction. """
def lowest_terms(numeratore, denominatore):
    mcd = math.gcd(numeratore, denominatore)
    risultato1 = numeratore / mcd
    risultato2 = denominatore / mcd
    print(round(risultato1), "-", round(risultato2))

def main():
    numeratore = int(input("Inserisci Numeratore: "))
    denominatore = int(input("Inserisci Denominatore: "))
    lowest_terms(numeratore, denominatore)

if __name__ == '__main__':
    main()
