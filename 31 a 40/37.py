""" Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message. """
lati = int(input("Inserisci il numero di Lati: "))
if lati == 0:
    print("E' un Cerchio.")
if lati == 3:
    print("E' un Triangolo.")
if lati == 4:
    print("Potrebbe essere un Quadrato, Rettangolo, Trapezio o Rombo..")
if lati == 5:
    print("E' un Pentagono.")
if lati == 6:
    print("E' un Esagono.")
if lati == 8:
    print("E' un Ottagono.")
if lati == 9:
    print("E' un Ennagono.")
if lati == 10:
    print("E' un Decagono.")
else:
    print("Non è una Forma Geometrica.")
