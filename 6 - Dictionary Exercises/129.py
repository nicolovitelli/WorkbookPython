import random

""" In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a function
that simulates rolling a pair of six-sided dice. Your function will not take any
parameters. It will return the total that was rolled on two dice as its only result.
Write a main program that uses your function to simulate rolling two six-sided
dice 1,000 times. As your program runs, it should count the number of times that each
total occurs. Then it should display a table that summarizes this data. Express the
frequency for each total as a percentage of the total number of rolls. Your program
should also display the percentage expected by probability theory for each total.
Sample output is shown below. """
def lancioPrimoDado():
    minimo = 1
    massimo = 6
    primo_dado = random.randint(minimo, massimo)
    print("\nPrimo Dado:", primo_dado)

def lancioSecondoDado():
    minimo = 1
    massimo = 6
    secondo_dado = random.randint(minimo, massimo)
    print("Secondo Dado:", secondo_dado)

def main():
    contatore = 0
    numeri = {}
    while contatore != 1000:
        lancioPrimoDado()
        lancioSecondoDado()
        contatore += 1
        numeri[lancioPrimoDado()] = lancioSecondoDado()
    print(numeri)
    
main()
