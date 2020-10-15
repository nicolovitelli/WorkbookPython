""" Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations. """
raggio = int(input("Inserisci il Raggio: "))
area = math.pi * (raggio ^ 2)
volume = 4/3 * math.pi * (raggio ^ 3)
print("L'Area del Cerchio è:", area)
print("Il Volume della Sfera è:", volume)
