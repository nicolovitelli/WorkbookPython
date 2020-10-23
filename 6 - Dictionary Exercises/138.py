""" A Bingo card consists of 5 columns of 5 numbers. The columns are labeled with the
letters B, I, N, G and O. There are 15 numbers that can appear under each letter. In
particular, the numbers that can appear under the B range from 1 to 15, the numbers
that can appear under the I range from 16 to 30, the numbers that can appear under
the N range from 31 to 45, and so on.
Write a function that creates a random Bingo card and stores it in a dictionary. The
keys will be the letters B, I, N, G and O. The values will be the lists of five numbers
that appear under each letter. Write a second function that displays the Bingo card
with the columns labeled appropriately. Use these functions to write a program that 
displays a random Bingo card. Ensure that the main program only runs when the file
containing your solution has not been imported into another program. """
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

def mostraCarta(carta):
    print("B I N G O")
    for i in range(5):
        for lettera in ["B", "I", "N", "G", "O"]:
            print(carta[lettera][i], end="")
        print()

def main():
    carta = creaCarta()
    mostraCarta(carta)

if __name__ == '__main__':
    main()
