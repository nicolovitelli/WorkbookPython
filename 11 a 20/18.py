""" The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place. """
raggio = float(input("Inserisci il Raggio: "))
altezza = float(input("Inserisci l'Altezza: "))
area = math.pi * (raggio ** 2)
volume = altezza * area
print("Il Volume del Cilindro è:", round(volume, 1))
