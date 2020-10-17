""" A particular zoo determines the price of admission based on the age of the guest.
Guests 2 years of age and less are admitted without charge. Children between 3 and
12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
for all other guests is $23.00.
Create a program that begins by reading the ages of all of the guests in a group
from the user, with one age entered on each line. The user will enter a blank line to
indicate that there are no more guests in the group. Then your program should display
the admission cost for the group with an appropriate message. The cost should be
displayed using two decimal places. """
eta = 1
prezzo = 0
tot_gruppo = 0
while eta != 0:
    eta = int(input("Inserisci Età: (0 per terminare) "))
    if eta > 65:
        prezzo = 18
        tot_gruppo = tot_gruppo + prezzo
    elif eta > 3 and eta < 12:
        prezzo = 14
        tot_gruppo = tot_gruppo + prezzo
    elif eta < 2:
        prezzo = 0
        tot_gruppo = tot_gruppo + prezzo
    else:
        prezzo = 23
        tot_gruppo = tot_gruppo + prezzo
print("Prezzo Totale:", tot_gruppo, "$")
