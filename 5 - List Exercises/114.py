import random

""" In order to win the top prize in a particular lottery, one must match all 6 numbers
on his or her ticket to the 6 numbers between 1 and 49 that are drawn by the lottery
organizer. Write a program that generates a random selection of 6 numbers for a
lottery ticket. Ensure that the 6 numbers selected do not contain any duplicates.
Display the numbers in ascending order. """
def lotteria():
    numero_minimo = 1
    numero_massimo = 49
    num_volte = 6
    ticket = []
    for i in range(num_volte):
        rand = random.randrange(numero_minimo, numero_massimo + 1)
        while rand in ticket:
            rand = random.randrange(numero_minimo, numero_massimo + 1)
        ticket.append(rand)
    ticket.sort()

    for n in ticket:
        print(n, end="")
    print()

def main():
    print("I Tuoi Numeri sono: ", end="")
    lotteria()
