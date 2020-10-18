""" In a particular jurisdiction, older license plates consist of three letters followed by
three numbers. When all of the license plates following that pattern had been used,
the format was changed to four numbers followed by three letters.
Write a function that generates a random license plate. Your function should have
approximately equal odds of generating a sequence of characters for an old license
plate or a new license plate. Write a main program that calls your function and
displays the randomly generated license plate. """
def targa_casuale():
    nuova_targa = 1
    vecchia_targa = 2
    targa = ""
    scelta = randint(1, 2)
    if scelta == 1:
        for i in range(3):
            lettera = random.choice(string.ascii_letters)
            targa = targa + lettera.upper()
        for i in range(3):
            numero = randint(1, 9)
            targa = targa + str(numero)
        print("La Targa (Vecchio Stile) generata è:", targa)
    else:
        for i in range(3):
            lettera = random.choice(string.ascii_letters)
            targa = targa + lettera.upper()
        for i in range(4):
            numero = randint(1, 9)
            targa = targa + str(numero)
        print("La Targa (Nuovo Stile) generata è:", targa)

def main():
    targa_casuale()

if __name__ == '__main__':
    main()
