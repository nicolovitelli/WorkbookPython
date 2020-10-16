""" In this exercise you will create a program that computes the average of a collection
of values entered by the user. The user will enter 0 as a sentinel value to indicate
that no further values will be provided. Your program should display an appropriate
error message if the first value entered by the user is 0. """
somma = 0.0
numero = 1
valore = 0
while (numero != 0):
    valore = int(input("Valore: "))
    somma = somma + valore
    numero = valore
if numero == 0:
    print("Fine")
    print("Somma", somma)
