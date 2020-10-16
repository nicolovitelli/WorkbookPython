""" Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters. """
in_per_ft = 12
cm_per_in = 2.54
print("Inserisci la tua altezza:")
feet = int(input(" Numero di piedi: "))
inches = int(input(" Numero di pollici: "))
cm = (feet * in_per_ft + inches) * cm_per_in
print("La tua altezza in centimetri è: ", cm)
