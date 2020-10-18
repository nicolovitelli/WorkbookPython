""" An online retailer provides express shipping for many of its items at a rate of $10.95
for the first item, and $2.95 for each subsequent item. Write a function that takes the
number of items in the order as its only parameter. Return the shipping charge for
the order as the function’s result. Include a main program that reads the number of
items purchased from the user and displays the shipping charge. """
def calcolo_item(numero):
    primo_oggetto = 10.95
    altri_oggetti = 2.95
    totale = (numero - 1) * altri_oggetti
    totale = totale + primo_oggetto
    return totale

numero = int(input("Inserisci Numero Item: "))
calcolo_item(numero)
