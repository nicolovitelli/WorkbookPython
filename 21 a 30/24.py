""" Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration. """
sec_per_minuto = 60
sec_per_ora = 3600
sec_per_giorno = 86400
giorni = int(input("Inserisci il numero di Giorni: "))
ore = int(input("Inserisci il numero di Ore: "))
minuti = int(input("Inserisci il numero di Minuti: "))
secondi = int(input("Inserisci il numero di Secondi: "))
secondi_totali = giorni * sec_per_giorno
secondi_totali = secondi_totali + (ore * sec_per_ora)
secondi_totali = secondi_totali + (minuti * sec_per_minuto)
secondi_totali = secondi_totali + secondi
print("Il numero totale dei Secondi è:", secondi_totali)
