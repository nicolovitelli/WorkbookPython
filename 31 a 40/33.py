""" A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. All of the
values should be displayed using two decimal places, and the decimal points in all
of the numbers should be aligned when reasonable values are entered by the user. """
costo_pane = 3.49
sconto = 60 # %
pane_acquistato = int(input("Inserisci la quantità di pane vecchio di un giorno acquistato: "))
# calcolo per: numero * percent / 100
prezzo_senzasconto = pane_acquistato * 3.49
prezzo_consconto = prezzo_senzasconto * 60 / 100
print("Prezzo del pane:", costo_pane)
print("Percentuale sconto:", sconto, "%")
print("Prezzo totale senza sconto:", prezzo_senzasconto, "$")
print("Totale da pagare con sconto:", round(prezzo_consconto,2), "$")
