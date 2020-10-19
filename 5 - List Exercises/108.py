""" Create a program that reads integers from the user until a blank line is entered. Once
all of the integers have been read your program should display all of the negative
numbers, followed by all of the zeros, followed by all of the positive numbers. Within
each group the numbers should be displayed in the same order that they were entered 
by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then
your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
should display each value on its own line."""
negativi = []
zero = []
positivi = []
numero = input("Inserisci Numero: ")
while numero != "":
    int(numero)
    if int(numero) < 0:
        negativi.append(numero)
    elif int(numero) == 0:
        zero.append(numero)
    elif int(numero) > 0:
        positivi.append(numero)
    numero = input("Inserisci Numero: ")
for numero in negativi:
    print(numero)
for numero in zero:
    print(numero)
for numero in positivi:
    print(numero)
