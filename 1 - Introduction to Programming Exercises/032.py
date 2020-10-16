""" Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value. """
num1 = int(input("Inserisci il primo numero: "))
num2 = int(input("Insersci il secondo numero: "))
num3 = int(input("Inserisci il terzo numero: "))
massimo = max(num1, num2, num3)
minimo = min(num1, num2, num3)
somma = num1 + num2 + num3
intermedio = (somma - minimo) - massimo
print("Ordine numeri: ", massimo, ",", intermedio, ",", minimo)
