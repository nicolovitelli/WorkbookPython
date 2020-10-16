""" In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG).
In Canada, fuel efficiency is normally expressed in liters-per-hundred
kilometers (L/100 km). Use your research skills to determine how to convert from
MPG to L/100 km. Then create a program that reads a value from the user in American
units and displays the equivalent fuel efficiency in Canadian units. """
miglia_per_gallone = 282.48
benzina_consumata = int(input("Inserisci la quantità di benzina consumata: "))
litri_per_100kilometri = miglia_per_gallone / benzina_consumata
print("Conversione di carburante effettuata: ", litri_per_100kilometri)
