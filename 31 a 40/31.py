""" Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number. For example, if the user enters 3141 then your program
should display 3+1+4+1=9. """
numero = int(input("Inserisci 4 cifre da sommare: "))
risultato = 0
while numero > 0:
    cifra = numero % 10
    risultato = risultato + cifra
    numero = numero // 10
print("La Somma delle 4 cifre è:", risultato)
