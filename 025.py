""" In this exercise you will reverse the process described in the previous exercise.
Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form
D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively.
The hours, minutes and seconds should all be formatted so that they occupy exactly two digits,
with a leading 0 displayed if necessary. """
sec_per_minuto = 60
sec_per_ora = 3600
sec_per_giorno = 86400
secondi = int(input("Inserisci il numero di Secondi: "))
giorni = secondi / sec_per_giorno
secondi = secondi % sec_per_giorno
ore = secondi / sec_per_ora
secondi = secondi % sec_per_ora
minuti = secondi / sec_per_minuto
secondi = secondi % sec_per_minuto
print("Conversione:\n",
      round(giorni), "giorno/i,", round(ore), "ore,", round(minuti), "minuti e", round(secondi), "secondi.")
