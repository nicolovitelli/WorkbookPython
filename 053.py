""" At a particular company, employees are rated at the end of each year. The rating scale
begins at 0.0, with higher values indicating better performance and resulting in larger
raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values
between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated
with each rating is shown in the following table. The amount of an employee’s raise
is $2400.00 multiplied by their rating. Write a program that reads a rating from the user
and indicates whether the performance was unacceptable, acceptable or meritorious.
The amount of the employee’s raise should also be reported.
Your program should display an appropriate error message if an invalid rating is entered."""
punteggio = float(input("Inserisci Punteggio Dipendente: "))
stipendio = 2400.00
inacettabile = 0.0
accettabile = 0.4
meritevole = 0.6
if punteggio == inacettabile:
    print("Perfomance Inaccettabile.")
    aumento = stipendio * inacettabile
    print("Totale Aumento:", aumento, "$")
    stipendio_tot = stipendio + aumento
    print("Totale Stipendio:", stipendio_tot, "$")
elif punteggio == accettabile:
    print("Perfomance Accettabile.")
    aumento = stipendio * accettabile
    print("Totale Aumento:", aumento, "$")
    stipendio_tot = stipendio + aumento
    print("Totale Stipendio:", stipendio_tot, "$")
elif punteggio >= meritevole:
    print("Perfomance Meritevole.")
    aumento = stipendio * meritevole
    print("Totale Aumento:", aumento, "$")
    stipendio_tot = stipendio + aumento
    print("Totale Stipendio:", stipendio_tot, "$")
else:
    print("Punteggio non valido.")
