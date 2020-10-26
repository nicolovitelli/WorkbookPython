""" Python uses the # character to mark the beginning of a comment. The comment ends
at the end of the line containing the # character. In this exercise, you will create a
program that removes all of the comments from a Python source file. Check each
line in the file to determine if a # character is present. If it is then your program
should remove all of the characters from the # character to the end of the line (we’ll
ignore the situation where the comment character occurs inside of a string). Save the
modified file using a new name that will be entered by the user. The user will also
enter the name of the input file. Ensure that an appropriate error message is displayed
if a problem is encountered while accessing the files. """
try:
    in_name = input("Inserisci Nome File: ")
    inf = open(in_name, "r")
    except:
        print("Errore")
        print("Sto uscendo..")
        quit()
    try:
        out_name = input("Inserisci nome file output: ")
        outf = open(out_name, "w")
    except:
        print("Errore con l'apertura del file")
        quit()
    try:
        for line in inf:
        pos = line.find("#")
        if pos > -1:
            line = line[0 : pos]
            line = line + "\n"
            outf.write(line)
        inf.close()
        outf.close()
    except:
        print("Errore")
        quit()
