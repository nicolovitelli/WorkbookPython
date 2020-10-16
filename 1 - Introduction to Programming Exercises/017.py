""" The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:
q = mCΔT.
Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change. """
water_heat_capacity = 4.186
electricity_price = 8.9
j_to_kwh = 2.777e-7
volume = float(input("Inserisci la quantità di Acqua in Millilitri: "))
d_temp = float(input("Inserisci l'aumento della Temperatura (gradi Celsius): "))
q = volume * d_temp * water_heat_capacity
print("Richiederà %d Joule di Energia." % q)
kwh = q * j_to_kwh
cost = kwh * electricity_price
print("Questa energia aggiuntiva costerà %.2f centesimi" % cost)
