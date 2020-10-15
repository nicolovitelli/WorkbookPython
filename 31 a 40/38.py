""" The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed. """
nome_mese = input("Inserisci il nome del Mese: ")
giorni = 31
if nome_mese == "Febbraio":
    giorni = "28 o 29"
    print("Il mese di", nome_mese, "ha", giorni, "giorni")
if nome_mese == "Aprile" or nome_mese == "Giugno" or nome_mese == "Settembre" or nome_mese == "Novembre":
    giorni = 30
print("Il mese di", nome_mese, "ha", giorni, "giorni")
