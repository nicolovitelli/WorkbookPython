""" Python’s standard library includes a method named count that determines how
many times a specific value occurs in a list. In this exercise, you will create a new
function named countRange which determines and returns the number of elements
within a list that are greater than or equal to some minimum value and less than some
maximum value. Your function will take three parameters: the list, the minimum
value and the maximum value. It will return an integer result greater than or equal to
0. Include a main program that demonstrates your function for several different lists,
minimum values and maximum values. Ensure that your program works correctly
for both lists of integers and lists of floating point numbers. """
def countRange(lista, minimo, massimo):
    contatore = 0
    for elementi in lista:
        if minimo <= elementi and elementi < massimo:
            contatore = contatore + 1
    print(contatore)
    return contatore

def main():
    lista = [1, 2, 3, 4, 5, 6, 7]
    minimo = 2
    massimo = 5
    countRange(lista, minimo, massimo)

main()
