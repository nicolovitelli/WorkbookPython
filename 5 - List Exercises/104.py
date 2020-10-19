""" Write a program that reads integers from the user and stores them in a list. Your
program should continue reading values until the user enters 0. Then it should display
all of the values entered by the user (except for the 0) in order from smallest to largest,
with one value appearing on each line. Use either the sort method or the sorted
function to sort the list. """
elenco = []
valore = int(input("Inserisci Valore nella Lista: "))
while valore != 0:
    elenco.append(valore)
    valore = int(input("Inserisci Valore nella Lista: "))
elenco.sort()
print("Elenco Valori Inseriti:", elenco)
