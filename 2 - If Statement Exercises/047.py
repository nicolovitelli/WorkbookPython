""" The horoscopes commonly reported in newspapers use the position of the sun at the
time of one’s birth to try and predict the future. This system of astrology divides the
year into twelve zodiac signs, as outline in the table below:
Write a program that asks the user to enter his or her month and day of birth. Then
your program should report the user’s zodiac sign as part of an appropriate output
message. """
mese = input("Inserisci il tuo Mese di Nascita: ")
giorno = int(input("Inserisci il tuo Giorno di Nascita: "))
if mese == "Dicembre":
    if giorno >= 22:
        print("Segno: Capricorno")
    else:
        print("Segno: Sagittario")
if mese == "Novembre":
    if giorno >= 22:
        print("Segno: Sagittario")
    else:
        print("Segno: Scorpione")
if mese == "Ottobre":
    if giorno >= 23:
        print("Segno: Scorpione")
    else:
        print("Segno: Bilancia")
if mese == "Settembre":
    if giorno >= 23:
        print("Segno: Bilancia")
    else:
        print("Vergine")
if mese == "Agosto":
    if giorno >= 23:
        print("Segno: Vergine")
    else:
        print("Segno: Leone")
if mese == "Luglio":
    if giorno >= 23:
        print("Segno: Leone")
    else:
        print("Segno: Cancro")
if mese == "Giugno":
    if giorno >= 22:
        print("Segno: Cancro")
    else:
        print("Segno: Gemelli")
if mese == "Maggio":
    if giorno >= 21:
        print("Segno: Gemelli")
    else:
        print("Segno: Toro")
if mese == "Aprile":
    if giorno >= 20:
        print("Segno: Toro")
    else:
        print("Ariete")
if mese == "Marzo":
    if giorno >= 21:
        print("Segno: Ariete")
    else:
        print("Segno: Pesci")
if mese == "Febbraio":
    if giorno >= 19:
        print("Segno: Pesci")
if mese == "Gennaio":
    if giorno >= 20:
        print("Segno: Acquario")
    else:
        print("Segno: Capricorno")
