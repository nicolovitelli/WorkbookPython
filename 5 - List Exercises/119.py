""" In many card games each player is dealt a specific number of cards after the deck
has been shuffled. Write a function, deal, which takes the number of hands, the
number of cards per hand, and a deck of cards as its three parameters. Your function
should return a list containing all of the hands that were dealt. Each hand will be
represented as a list of cards.
When dealing the hands, your function should modify the deck of cards passed
to it as a parameter, removing each card from the deck as it is added to a player’s
hand. When cards are dealt, it is customary to give each player a card before any
player receives an additional card. Your function should follow this custom when
constructing the hands for the players.
Use your solution to Exercise 118 to help you construct a main program that
creates and shuffles a deck of cards, and then deals out four hands of five cards each.
Display all of the hands of cards, along with the cards remaining in the deck after
the hands have been dealt. """
carte = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
segno = ["s", "h", "d", "c"]
mazzo = []
def createDeck():
    contatore = 0
    while contatore != 52:
        carta_casuale = random.choice(carte)
        segno_casuale = random.choice(segno)
        mazzo.append(carta_casuale)
        mazzo.append(segno_casuale)
        contatore = contatore + 1
    return mazzo

def deal(mani, num_carte, mazzo):
    contatore = 0
    for contatore in range(mani):
        for conta2 in range(num_carte):
            print(mazzo[contatore])
            contatore = contatore + 1

def main():
    mani = int(input("Inserisci Numero di Mani: "))
    num_carte = int(input("Inserisci Numero di Carta per mano: "))
    mazzo = createDeck()
    deal(mani, num_carte, mazzo)

main()
