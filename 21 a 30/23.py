import math
""" A polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides: area = n × s2 / 4 × tan π n
Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values."""
s = float(input("Inserisci la Lunghezza del Lato: "))
n = int(input("Inserisci il numero di Lati: "))
area = n * (s ** 2) / 4 * math.tan(math.pi / n)
print("L'Area del Poligono è:", round(area))
