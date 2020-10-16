""" It is common for images of a country’s previous leaders, or other individuals of historical significance,
to appear on its money. The individuals that appear on banknotes in the United States are listed in Table 2.1.
Write a program that begins by reading the denomination of a banknote from the
user. Then your program should display the name of the individual that appears on the banknote of the entered amount.
An appropriate error message should be displayed if no such note exists. """
banconota = int(input("Inserisci valore banconota: "))
un_d = "George Washington"
due_d = "Thomas Jefferson"
cin_d = "Abraham Lincoln"
die_d = "Alexander Hamilton"
ven_d = "Andrew Jackson"
cinq_d = "Ulysses S. Grant"
cen_d = "Benjamin Franklin"
if banconota == 1:
    print("Sulla Banconota da", banconota, "$ è rappresentato", un_d)
elif banconota == 2:
    print("Sulla Banconota da", banconota, "$ è rappresentato", due_d)
elif banconota == 5:
    print("Sulla Banconota da", banconota, "$ è rappresentato", cin_d)
elif banconota == 10:
    print("Sulla Banconota da", banconota, "$ è rappresentato", die_d)
elif banconota == 20:
    print("Sulla Banconota da", banconota, "$ è rappresentato", ven_d)
elif banconota == 50:
    print("Sulla Banconota da", banconota, "$ è rappresentato", cinq_d)
elif banconota == 100:
    print("Sulla Banconota da", banconota, "$ è rappresentato", cen_d)
else:
    print("Non Esistente.")
