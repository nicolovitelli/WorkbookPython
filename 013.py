""" Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies. """
centesimi_per_toonie = 200
centesimi_per_loonie = 100
centesimi_per_quarter = 25
centesimi_per_dime = 10
centesimi_per_nickel = 5
centesimi = int(input("Inserisci il numero di centesimi: "))
print(" ", centesimi // centesimi_per_toonie, "toonies")
centesimi = centesimi % centesimi_per_toonie
print(" ", centesimi // centesimi_per_loonie, "loonies")
centesimi = centesimi % centesimi_per_loonie
print(" ", centesimi // centesimi_per_quarter, "quarters")
centesimi = centesimi % centesimi_per_quarter
print(" ", centesimi // centesimi_per_dime, "dimes")
centesimi = centesimi % centesimi_per_dime
print(" ", centesimi // centesimi_per_nickel, "nickels")
centesimi = centesimi % centesimi_per_nickel
print(" ", centesimi, "pennies")
