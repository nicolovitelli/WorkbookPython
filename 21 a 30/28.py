""" When the wind blows in cold weather, the air feels even colder than it actually is
because the movement of the air increases the rate of cooling for warm objects, like
people. This effect is known as wind chill.
In 2001, Canada, the United Kingdom and the United States adopted the following formula
for computing the wind chill index. Within the formula Ta is the
air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
A similar formula with different constant values can be used with temperatures in
degrees Fahrenheit and wind speeds in miles per hour.
WCI = 13.12 + 0.6215Ta − 11.37V0.16 + 0.3965TaV0.16
Write a program that begins by reading the air temperature and wind speed from the
user. Once these values have been read your program should display the wind chill
index rounded to the closest integer. """
wc_offset = 13.12
wc_fattore1 = 0.6215
wc_fattore2 = -11.37
wc_fattore3 = 0.3965
wc_esponente = 0.16
temperatura = float(input("Inserisci la Temperatura dell'aria in gradi Celsius: "))
velocita = float(input("Inserisci la velocità del vento (in km/h): "))
wci = wc_offset +\
      wc_fattore1 * temperatura +\
      wc_fattore2 + velocita ** wc_esponente +\
      wc_fattore3 * temperatura * velocita ** wc_esponente
print("Indice di Wind Chill: ", round(wci))
