""" Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the internet. """
temperatura_celsius = float(input("Inserisci la Temperatura in gradi Celsius: "))
temperatura_fahrenheit = 1.8 * temperatura_celsius + 32
temperatura_kelvin = 273.15 * temperatura_celsius
print("%.2f gradi Celsius corrispondono a:\n %0.2f gradi Fahrenheit e %0.2f gradi Kelvin" %
      (temperatura_celsius, temperatura_fahrenheit, temperatura_kelvin))
