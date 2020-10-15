""" In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized. """
piedi = int(input("Inserisci la misura in Piedi: "))
pollici_per_piede = 12
yard_per_piede = 0.3
miglia_per_piede = 0.000189394
pollici = piedi * pollici_per_piede
yard = piedi / yard_per_piede
miglia = piedi / miglia_per_piede
print("Misura in Pollici:", pollici)
print("Misura in Yard:", yard)
print("Misura in Miglia:", miglia)
