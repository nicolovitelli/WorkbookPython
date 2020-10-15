import math
""" In the previous exercise you created a program that computed the area of a triangle
when the length of its base and its height were known. It is also possible to compute
the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
can be calculated using the following formula: area = s × (s − s1) × (s − s2) × (s − s3)
Develop a program that reads the lengths of the sides of a triangle from the user and
displays its area. """
lato1 = float(input("Inserisci Lunghezza del primo lato: "))
lato2 = float(input("Inserisci Lunghezza del secondo lato: "))
lato3 = float(input("Inserisci Lunghezza del terzo lato: "))
s = (lato1 + lato2 + lato3) / 2
area = math.sqrt(s * (s - lato1) * (s - lato2) * (s - lato3))
print("L'Area del Triangolo è:", round(area))
