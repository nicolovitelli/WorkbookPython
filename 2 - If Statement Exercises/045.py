"""Positions on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row, as shown below: Write a program that reads a position from the user.
Use an if statement to determine if the column begins with a black square or a white square. Then use modular
arithmetic to report the color of the square in that row. For example, if the user enters
a1 then your program should report that the square is black. If the user enters d5
then your program should report that the square is white. Your program may assume
that a valid position will always be entered. It does not need to perform any error
checking. """
colonna = input("Inserisci la lettera della colonna: ")
riga = int(input("Inserisci il numero della riga: "))
scacchi = [colonna, riga]
b = "Casella Bianca"
n = "Casella Nera"
if scacchi[0] == "a" and scacchi[1] % 2 == 0:
    print(b)
elif scacchi[0] == "b" and scacchi[1] % 2 == 0:
    print(b)
elif scacchi[0] == "c" and scacchi[1] % 2 == 0:
    print(b)
elif scacchi[0] == "d" and scacchi[1] % 2 == 0:
    print(b)
elif scacchi[0] == "e" and scacchi[1] % 2 == 0:
    print(b)
elif scacchi[0] == "f" and scacchi[1] % 2 == 0:
    print(b)
elif scacchi[0] == "g" and scacchi[1] % 2 == 0:
    print(b)
elif scacchi[0] == "h" and scacchi[1] % 2 == 0:
    print(b)
elif scacchi[0] == "a" and scacchi[1] % 2 != 0:
    print(n)
elif scacchi[0] == "b" and scacchi[1] % 2 != 0:
    print(n)
elif scacchi[0] == "c" and scacchi[1] % 2 != 0:
    print(n)
elif scacchi[0] == "d" and scacchi[1] % 2 != 0:
    print(n)
elif scacchi[0] == "f" and scacchi[1] % 2 != 0:
    print(n)
elif scacchi[0] == "g" and scacchi[1] % 2 != 0:
    print(n)
elif scacchi[0] == "h" and scacchi[1] % 2 != 0:
    print(n)
