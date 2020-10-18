import math

""" Write a function that takes the lengths of the two shorter sides of a right triangle as
its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
theorem, as the function’s result. Include a main program that reads the lengths of
the shorter sides of a right triangle from the user, uses your function to compute the
length of the hypotenuse, and displays the result. """
def ipotenusa_triangolo(lato1, lato2):
    ipotenusa = math.sqrt((lato1 ** 2) + (lato2 ** 2))
    print("L'Ipotenusa è uguale a:", round(ipotenusa,2))

lato1 = float(input("Inserisci lunghezza Lato 1: "))
lato2 = float(input("Inserisci Lunghezza Lato 2: "))
ipotenusa_triangolo(lato1, lato2)
