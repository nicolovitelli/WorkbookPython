""" At a particular university, letter grades are mapped to grade points in the following
manner: Write a program that begins by reading a letter grade from the user. Then your
program should compute and display the equivalent number of grade points. Ensure that your program generates
an appropriate error message if the user enters an invalid letter grade."""
lettera = input("Inserisci Lettera: ")
if lettera == "A+":
    print("Punti: 4.0")
elif lettera == "A":
    print("Punti: 4.0")
elif lettera == "A-":
    print("Punti: 3.7")
elif lettera == "B+":
    print("Punti: 3.3")
elif lettera == "B":
    print("Punti: 3.0")
elif lettera == "B-":
    print("Punti: 2.7")
elif lettera == "C+":
    print("Punti: 2.3")
elif lettera == "C":
    print("Punti: 2.0")
elif lettera == "C-":
    print("Punti: 1.7")
elif lettera == "D+":
    print("Punti: 1.3")
elif lettera == "D":
    print("Punti: 1.0")
elif lettera == "F":
    print("Punti: 0")
else:
    print("Lettera non valida.")
