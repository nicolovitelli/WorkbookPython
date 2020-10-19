""" When analysing data collected as part of a science experiment it may be desirable
to remove the most extreme values before performing other calculations. Write a
function that takes a list of values and an non-negative integer, n, as its parameters.
The function should create a new copy of the list with the n largest elements and the
n smallest elements removed. Then it should return the new copy of the list as the
function’s only result. The order of the elements in the returned list does not have to
match the order of the elements in the original list.
Write a main program that demonstrates your function. Your function should read
a list of numbers from the user and remove the two largest and two smallest values
from it. Display the list with the outliers removed, followed by the original list. Your
program should generate an appropriate error message if the user enters less than 4 values. """
def rimuovi_elementi(elenco):
    massimo = max(elenco)
    minimo = min(elenco)
    print(massimo, minimo)
    nuova_lista = elenco
    nuova_lista.pop(massimo)
    nuova_lista.pop(minimo)
    return nuova_lista

def main():
    elenco = []
    valore = int(input("Inserisci Valore nella Lista: "))
    while valore != 0:
        numero = float(valore)
        elenco.append(numero)
        valore = int(input("Inserisci Valore nella Lista: "))
    if len(elenco) < 4:
        print("Non hai inserito abbastanza Valori")
    else:
        print(rimuovi_elementi(elenco))
        print("Lista Originale:", elenco)

main()


# in errore
