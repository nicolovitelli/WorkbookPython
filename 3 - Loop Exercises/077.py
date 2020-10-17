""" Write a program that converts a binary (base 2) number to decimal (base 10). Your
program should begin by reading the binary number from the user as a string. Then
it should compute the equivalent decimal number by processing each digit in the
binary number. Finally, your program should display the equivalent decimal number
with an appropriate message. """
binario = input("Inserisci numbero binario: ")
cifra = len(binario)
decimale = 0
for i in range(len(binario)):
    val_decimale = (binario[i] * (2 ** cifra))
    decimale = decimale + int(val_decimale)
    cifra = cifra - 1
    print(decimale)
 # errato, non completo
