""" Write a program that reads integers from the user and stores them in a list. Use 0 as
a sentinel value to mark the end of the input. Once all of the values have been read
your program should display them (except for the 0) in reverse order, with one value
appearing on each line. """
elenco = []
valore = int(input("Inserisci Valore nella Lista: "))
while valore != 0:
    elenco.append(valore)
    valore = int(input("Inserisci Valore nella Lista: "))
elenco.reverse()
print("Elenco Valori Inseriti:")
for valore in elenco:
    print(valore)
