""" Using the definition of a sublist from Exercise 125, write a function that returns a list
containing every possible sublist of a list. For example, the sublists of [1, 2, 3]
are [], [1], [2], [3], [1, 2], [2, 3] and [1, 2, 3]. Note that your function will always return a list containing
at least the empty list because the empty list is a sublist of every list.
Include a main program that demonstrate your function by displaying all of the sublists of several different lists. """
def sottoliste(lista):
    sottolista = [[]]
    for lunghezza in range(1, len(lista) + 1):
        for i in range(0, len(lista) - lunghezza + 1):
            sottolista.append(lista[i : i + lunghezza])
    return sottolista

def main():
    print("Le Sottoliste di [] sono:")
    print(sottoliste([]))

    print("Le Sottoliste di [1] sono:")
    print(sottoliste([1]))

    print("Le Sottoliste di [1, 2] sono:")
    print(sottoliste([1, 2]))

    print("Le Sottoliste di [1, 2, 3] sono:")
    print(sottoliste([1, 2, 3]))

    print("Le Sottoliste di [1, 2, 3, 4] sono:")
    print(sottoliste([1, 2, 3, 4]))

main()
