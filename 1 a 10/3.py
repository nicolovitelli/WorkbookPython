""" Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with. """
l = input("Inserisci la Larghezza: ")
l1 = input("Inserisci la Lunghezza: ")
larghezza = float(l)
lunghezza = float(l1)
area = larghezza * lunghezza
print(area)
