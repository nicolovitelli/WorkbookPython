""" The year is divided into four seasons: spring, summer, fall and winter. While the
exact dates that the seasons change vary a little bit from year to year because of the
way that the calendar is constructed, we will use the following dates for this exercise: 
Create a program that reads a month and day from the user. The user will enter
the name of the month as a string, followed by the day within the month as an
integer. Then your program should display the season associated with the date that
was entered. """
primavera = ["Marzo", 20]
estate = ["Giugno", 21]
autunno = ["Settembre", 22]
inverno = ["Dicembre", 21]
mese = input("Inserisci il Mese: ")
giorno = int(input("Inserisci il Giorno: "))
stagione = [mese, giorno]
if mese == "Gennaio" or mese == "Febbraio":
    print("Stagione: Inverno")
elif mese == "Marzo":
    if giorno < 20:
        print("Stagione: Inverno")
    else:
        print("Stagione: Primavera")
elif mese == "Aprile" or mese == "Maggio":
    print("Stagione: Primavera")
elif mese == "Giugno":
    if giorno < 21:
        print("Stagione: Primavera")
    else:
        print("Stagione: Estate")
elif mese == "Luglio" or mese == "Agosto":
    print("Stagione: Estate")
elif mese == "Settembre":
    if giorno < 22:
        print("Stagione: Estate")
    else:
        print("Stagione: Autunno")
elif mese == "Ottobre" or mese == "Novembre":
    print("Stagione: Autunno")
elif mese == "Dicembre":
    if giorno < 21:
        print("Stagione: Autunno")
    else:
        print("Stagione: Inverno")
