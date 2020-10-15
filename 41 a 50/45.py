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
