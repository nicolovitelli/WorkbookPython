from random import randrange

""" What’s the minimum number of times you have to flip a coin before you can have
three consecutive flips that result in the same outcome (either all three are heads or
all three are tails)? What’s the maximum number of flips that might be needed? How
many flips are needed on average? In this exercise we will explore these questions
by creating a program that simulates several series of coin flips.
Create a program that uses Python’s random number generator to simulate flipping
a coin several times. The simulated coin should be fair, meaning that the probability
of heads is equal to the probability of tails. Your program should flip simulated
coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each
time the outcome is heads, and a T each time the outcome is tails, with all of the
outcomes shown on the same line. Then display the number of flips needed to reach
3 consecutive flips with the same outcome. When your program is run it should
perform the simulation 10 times and report the average number of flips needed. """
testa = 1
croce = 2
interrompi = 0
contatore = 0
while interrompi == 0:
    lancio = randrange(0, 3)
    print(lancio, end=" ")
    contatore = contatore + 1
    primo_lancio = lancio
    lancio = randrange(0, 3)
    print(lancio, end=" ")
    contatore = contatore + 1
    secondo_lancio = lancio
    lancio = randrange(0, 3)
    print(lancio, end=" ")
    contatore = contatore + 1
    terzo_lancio = lancio
    if primo_lancio == secondo_lancio and secondo_lancio == terzo_lancio:
        print("Terminato, ci sono voluti", contatore, "lanci")
        interrompi = 1
        

