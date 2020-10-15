""" The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
shown in the table below. The pattern repeats from there, with 2012 being another
year of the dragon, and 1999 being another year of the hare. 
Write a program that reads a year from the user and displays the animal associated
with that year. Your program should work correctly for any year greater than or equal
to zero, not just the ones listed in the table. """
anno = int(input("Inserisci Anno: "))
if anno % 12 == 8:
    print("Animale: Dragone")
elif anno % 12 == 9:
    print("Animale: Serpente")
elif anno % 12 == 10:
    print("Animale: Cavallo")
elif anno % 12 == 11:
    print("Animale: Pecora")
elif anno % 12 == 0:
    print("Animale: Scimmia")
elif anno % 12 == 1:
    print("Animale: Gallina")
elif anno % 12 == 2:
    print("Animale: Cane")
elif anno % 12 == 3:
    print("Animale: Maiale")
elif anno % 12 == 4:
    print("Animale: Topo")
elif anno % 12 == 5:
    print("Animale: Bue")
elif anno % 12 == 6:
    print("Animale: Tigre")
elif anno % 12 == 7:
    print("Animale: Lepre")
