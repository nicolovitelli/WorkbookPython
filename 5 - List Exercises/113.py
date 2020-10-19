""" When writing out a list of items in English, one normally separates the items with
commas. In addition, the word “and” is normally included before the last item, unless
the list only contains one item. Write a function that takes a list of strings as its only parameter.
Your function should return a string that contains all of the items in the list formatted in the manner
described previously as its only result. While the examples shown previously only
include lists containing four elements or less, your function should behave correctly
for lists of any length. Include a main program that reads several items from the user,
formats them by calling your function, and then displays the result returned by the function."""
def formattare_lista(lista):
    if len(lista) == 0:
        return "lista vuota"
    if len(lista) == 1:
        return str(lista[0])
    risultato = ""
    for i in range(0, len(lista) - 2):
        risultato = risultato + str(lista[i]) + ", "
    risultato = risultato + str(lista[len(lista - 2)]) + " and "
    risultato = risultato + str(lista[len(lista - 1)])
    return risultato

def main():
    lista = []
    oggetto = input("Inserisci un Oggetto: ")
    while oggetto != "":
        lista.append(oggetto)
        oggetto = input("Inserisci un Oggetto: ")
    print("Gli Oggetti sono:", formattare_lista(lista))

main()
