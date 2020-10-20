""" Write a function that determines whether or not a list of values is in sorted order
(either ascending or descending). The function should return True if the list is
already sorted. Otherwise it should return False. Write a main program that reads
a list of numbers from the user and then uses your function to report whether or not
the list is sorted. """
def controllo_lista(lista):
    nuova_lista = []
    nuova_lista = lista.sort()
    print(nuova_lista)
    var = False
    elemento = 0
    for elemento in lista:
        if nuova_lista[elemento] == lista[elemento]:
            var = True
        else:
            var = False
    if var:
        print("Lista Ordinata")
    elif len(lista) == 0:
        print("Lista con 0 Elementi")
        return False
    elif len(lista) == 1:
        print("Lista con un solo Elemento")
        return False
    else:
        print("Lista Non Ordinata")

def main():
    elemento = (input("Inserisci Primo Elemento della Lista: "))
    elemento = int(elemento)
    lista = []
    while elemento != "":
        lista.append(elemento)
        elemento = input("Inserisci Primo Elemento della Lista: ")
        elemento = int(elemento)
    controllo_lista(lista)

if __name__ == '__main__':
    main()
    
    #ERRORE: ValueError: invalid literal for int() with base 10: '' (elemento = int(elemento)
