""" A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle. """
lato1 = float(input("Inserisci Lunghezza del primo lato: "))
lato2 = float(input("Inserisci Lunghezza del secondo lato: "))
lato3 = float(input("Inserisci Lunghezza del terzo lato: "))
if lato1 == lato2 and lato2 == lato3:
    print("E' un Triangolo Equilatero.")
if lato1 == lato2 and lato2 != lato3 or lato1 == lato3 and lato2 != lato3 or lato2 == lato3 and lato1 != lato2:
    print("E' un Triangolo Isoscele.")
if lato1 != lato2 and lato2 != lato3 and lato1 != lato3:
    print("E' un Triangolo Scaleno.")
