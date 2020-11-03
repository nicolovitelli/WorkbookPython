""" The ideal gas law is a mathematical approximation of the behavior of gasses as
pressure, volume and temperature change. It is usually stated as:
PV = nRT
where P is the pressure in Pascals, V is the volume in liters, n is the amount of
substance in moles, R is the ideal gas constant, equal to 8.314 J
mol K , and T is the
temperature in degrees Kelvin.
Write a program that computes the amount of gas in moles when the user supplies
the pressure, volume and temperature. Test your program by determining the number
of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
approximately 20 degrees Celsius or 68 degrees Fahrenheit. """
pressione = float(input("Inserisci Pressione: "))
volume = float(input("Inserisci il Volume: "))
temperatura = float(input("Inserisci la Temperatura: "))
r = 8.31
igl = pressione * volume
ig2 = r * temperatura
print(igl, "=", round(ig2,2))
scuba = 20.000,00 * 12
scuba_celsius = r * 20
scuba_far = r * 68
print(scuba, "=", round(scuba_celsius,2), "(gradi Celsius)")
print(scuba, "=", round(scuba_far,2), "(gradi Fahrenheit)")
