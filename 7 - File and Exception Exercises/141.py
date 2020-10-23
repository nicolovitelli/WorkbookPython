import sys
# ESERCIZIO 141
""" Unix-based operating systems usually include a tool named head. It displays the
first 10 lines of a file whose name is provided as a command line parameter. Write
a Python program that provides the same behavior. Display an appropriate error
message if the file requested by the user does not exist or if the command line
parameter is omitted."""
numero_rige = 10
contatore = 0
if len(sys.argv) != 2:
    print("Devi inserire il il nome del file come parametro.")
    quit()
try:
    inf = open(sys.argv[1], "r")
    line = inf.readline()
    count = 0
    while count < numero_rige and line != "":
        line = line.rstrip()
        contatore = contatore + 1
        print(line)
        line = inf.readline()
        inf.close()
except IOError:
    print("Errore durante l'accesso al File")
