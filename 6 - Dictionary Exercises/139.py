""" Create a main program that demonstrates your function by creating several Bingo
cards, displaying them, and indicating whether or not they contain a winning line.
You should demonstrate your function with at least one card with a horizontal line,
at least one card with a vertical line, at least one card with a diagonal line, and at
least one card that has some numbers crossed out but does not contain a winning line.
You will probably want to import your solution to Exercise 138 when completing
this exercise. """
numeri_per_lettera = 15
def creaCarta():
    carta = {}
    lower = 1
    upper = 1 + numeri_per_lettera
    for lettera in ["B", "I", "N", "G", "O"]:
        carta[lettera] = []
        while len(carta[lettera]) != 5:
            num_successivo = random.randrange(lower, upper)
            if num_successivo not in carta[lettera]:
                carta[lettera].append(num_successivo)
        lower = lower + numeri_per_lettera
        upper = upper + numeri_per_lettera
    return carta

def controllaCarta(carta):
    contatore = 0
    for numero in carta:
        if carta[numero] == 0:
            contatore = contatore + 1
    if contatore > 5:
        print("Carta Vincitrice")
        return True
    else:
        print("Carta Perdente")
        return False

def main():
    carta = creaCarta()
    controllaCarta(carta)

if __name__ == '__main__':
    main()
