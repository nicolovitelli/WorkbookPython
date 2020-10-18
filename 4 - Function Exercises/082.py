""" In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25
for every 140 meters traveled. Write a function that takes the distance traveled (in
kilometers) as its only parameter and returns the total fare as its only result. Write a
main program that demonstrates the function. """
def calcola_prezzo(distanza):
    prezzo_base = 4
    prezzo_140metri = 0.25
    tot_distanza = (distanza * 1000) // 140
    tot_prezzo = tot_distanza * prezzo_140metri
    tot_prezzo = tot_prezzo + prezzo_base
    return tot_prezzo

distanza = int(input("inserisci distanza in km: "))
calcola_prezzo(distanza)
