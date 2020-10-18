""" Write a function that takes three numbers as parameters, and returns the median value
of those parameters as its result. Include a main program that reads three values from
the user and displays their median. """
def media_valori(primo, secondo, terzo):
    somma = primo + secondo + terzo
    media = somma / 3
    return media

primo = int(input("Inserisci il primo numero: "))
secondo = int(input("Inserisci il secondo numero: "))
terzo = int(input("Inserisci il terzo numero: "))
media_valori(primo, secondo, terzo)
