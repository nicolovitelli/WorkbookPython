import math

""" The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2)) 
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers. """
t1 = float(input("Latitudine 1: "))
g1 = float(input("Latitudine 2: "))
t2 = float(input("Longitudine 1: "))
g2 = float(input("Longitudine 2: "))
distanza = 6371.01 * math.acos((math.sin(t1)) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
print("La Distanza tra i due punti è di:", distanza, "km")
