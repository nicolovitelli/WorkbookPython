""" Canada has three national holidays which fall on the same dates each year. 
Write a program that reads a month and day from the user. If the month and day
match one of the holidays listed previously then your program should display the
holiday’s name. Otherwise your program should indicate that the entered month and
day do not correspond to a fixed-date holiday. """
mese = int(input("Inserisci il Mese (cifra): "))
giorno = int(input("Inserisci il Giorno (cifra): "))
mes_gio = [mese, giorno]
nuovo_anno = [1, 1]
canada_day = [7, 1]
natale = [12, 25]
if mes_gio == nuovo_anno:
    print("Festività: Nuovo Anno")
elif mes_gio == canada_day:
    print("Festività: Canada Day")
elif mes_gio == natale:
    print("Festività: Natale")
else:
    print("Nessuna festività trovata.")
