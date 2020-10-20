""" A standard deck of playing cards contains 52 cards. Each card has one of four suits
along with a value. The suits are normally spades, hearts, diamonds and clubs while
the values are 2 through 10, Jack, Queen, King and Ace.
Each playing card can be represented using two characters. The first character is
the value of the card, with the values 2 through 9 being represented directly. The
characters “T”, “J”, “Q”, “K” and “A” are used to represent the values 10, Jack,
Queen, King and Ace respectively. The second character is used to represent the suit
of the card. It is normally a lowercase letter: “s” for spades, “h” for hearts, “d” for
diamonds and “c” for clubs. The following table provides several examples of cards
and their two-character representations. """
def createDeck():
    carte = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    segno = ["s", "h", "d", "c"]
    carta = []
    contatore = 0
    while contatore != 52:
        carta_casuale = random.choice(carte)
        segno_casuale = random.choice(segno)
        carta.append(carta_casuale)
        carta.append(segno_casuale)
        print(carta[contatore], "\n")
        contatore = contatore + 1
def main():
    print("Mescolamento carte in corso..")
    createDeck()

main()
