""" Write a program that reads numbers from the user until a blank line is entered. Your
program should display the average of all of the values entered by the user. Then
the program should display all of the below average values, followed by all of the
average values (if any), followed by all of the above average values. An appropriate
label should be displayed before each list of values. """
numeri = []
numero = input("Inserisci Numero: ")
while numero != "":
    if int(numero) not in numeri:
        numeri.append(int(numero))
    numero = input("Inserisci Numero: ")
media_numeri = sum(numeri) / len(numeri)
print("Media:", media_numeri)
print("Numeri al di sotto della Media:")
for numero in numeri:
    if numero < media_numeri:
        print(numero)
print("Numeri al di sopra della Media:")
for numero in numeri:
    if numero > media_numeri:
        print(numero)
