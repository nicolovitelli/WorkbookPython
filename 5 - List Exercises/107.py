""" In this exercise, you will create a program that reads words from the user until the
user enters a blank line. After the user enters a blank line your program should display each word entered by the user
exactly once. The words should be displayed in the same order that they were entered. """
parole = []
parola = input("Inserisci una Parola: ")
while parola != "":
    if parola not in parole:
        parole.append(parola)
    parola = input("Inserisci una Parola: ")
for parola in parole:
    print(parola)
