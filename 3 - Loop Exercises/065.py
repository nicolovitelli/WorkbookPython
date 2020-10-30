import math

""" Write a program that computes the perimeter of a polygon. Begin by reading the x
and y values for the first point on the perimeter of the polygon from the user. Then
continue reading pairs of x and y values until the user enters a blank line for the
x-coordinate. Each time you read an additional coordinate you should compute the
distance to the previous point and add it to the perimeter. When a blank line is entered
for the x-coordinate your program should add the distance from the last point back
to the first point to the perimeter. Then it should display the total perimeter. Sample
input and output is shown below, with user input shown in bold:  """
perimetro = 0
prima_x = float(input("Inserisci la X: "))
prima_y = float(input("Inserisci la Y: "))
x_prec = prima_x
y_prec = prima_y
riga = input("Inserisci la X (vuoto per uscire): ")
while riga != "":
    x = float(riga)
    y = float(input("Inserisci la Y: "))
    distanza = sqrt((x_prec - x) ** 2 + (y_prec - y) ** 2)
    perimetro = perimetro + distanza
    x_prec = x
    y_prec = y
    riga = input("Inserisci la X (vuoto per uscire): ")
distanza = sqrt((prima_x - x) ** 2 + (prima_y - y) ** 2)
perimetro = perimetro + distanza
print("Il Perimetro del Poligono è:", perimetro)
