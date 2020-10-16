""" A particular cell phone plan includes 50 minutes of air time and 50 text messages
for $15.00 a month. Each additional minute of air time costs $0.25, while additional
text messages cost $0.15 each. All cell phone bills include an additional charge of
$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
subject to 5 percent sales tax. Write a program that reads the number of minutes and text messages used in a
month from the user. Display the base charge, additional minutes charge (if any),
additional text message charge (if any), the 911 fee, tax and total bill amount. Only
display the additional minute and text message charges if the user incurred costs in
these categories. Ensure that all of the charges are displayed using 2 decimal places. """
minuti_usati = int(input("Inserisci il numero di Minuti usati: "))
messaggi_usati = int(input("Inserisci il numero di Messaggi usati: "))
messaggi = 50
minuti = 50
tot_costo = 15 #$ al mese
minuto_extra = 0.25
messaggio_extra = 0.15
tassa_911 = 0.44
tassa = 5 # %
if minuti_usati > minuti:
    minuti_usati = minuti_usati - minuti
    print("Hai usato", minuti_usati, "minuti Extra.")
    print("-----------------")
    costo_min = minuti_usati * 0.25
    print("Costo Minuti Extra:", costo_min, "$")
    tot_costo = tot_costo + costo_min
if messaggi_usati > messaggi:
    messaggi_usati = messaggi_usati - messaggi
    print("Hai usato", messaggi_usati, "messaggi Extra.")
    print("-----------------")
    costo_mes = messaggi_usati * 0.15
    print("Costo Messaggi Extra:", costo_mes, "$")
    tot_costo = tot_costo + costo_mes
# 20% di 30 = 30 * 20 / 100
tot_costo = tot_costo + tassa_911
perc_tasse = tot_costo * 5 / 100
tot_costo = tot_costo + perc_tasse
print("Costo Base: 15 $")
print("Percentuale Tasse:", tassa, "%")
print("Tassa 911:", tassa_911, "$")
print("-----------------")
print("Totale da pagare:", round(tot_costo, 2), "$")
