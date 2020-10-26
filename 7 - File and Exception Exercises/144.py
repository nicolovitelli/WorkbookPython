""" Create a program that adds line numbers to a file. The name of the input file will be
read from the user, as will the name of the new file that your program will create.
Each line in the output file should begin with the line number, followed by a colon
and a space, followed by the line from the input file. """
nome_file = input("Inserisci Nome File: ")
file_object = open (nome_file, 'a')
riga = input("Inserisci Riga 1: ")
file_object.write(riga)
contatore = 2
while riga != "":
    file_object.write(riga)
    riga = input("Inserisci Riga: ")
print("Righe Inserite")
