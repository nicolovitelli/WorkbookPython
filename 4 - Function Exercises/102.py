""" Many recipe books still use cups, tablespoons and teaspoons to describe the volumes
of ingredients used when cooking or baking. While such recipes are easy enough to
follow if you have the appropriate measuring cups and spoons, they can be difficult
to double, triple or quadruple when cooking Christmas dinner for the entire extended
family. For example, a recipe that calls for 4 tablespoons of an ingredient requires 16
tablespoons when quadrupled. However, 16 tablespoons would be better expressed
(and easier to measure) as 1 cup. Write a function that expresses an imperial volume
using the largest units possible. The function will take the number of units as its first parameter,
and the unit of measure (cup, tablespoon or teaspoon) as its second parameter. Return a string
representing the measure using the largest possible units as the function’s only result. """
cucchiaini_per_cucchiai = 3
cucchiaini_per_tazza = 48
def riduciMisura(numero, unita):
    unita = unita.lower()
    if unita == "cucchiaino" or unita == "cucchiaini":
        cucchiaini = numero
    elif unita == "cucchiai" or unita == "cucchiaini":
        cucchiaini = numero * cucchiaini_per_cucchiai
    elif unita == "tazza" or unita == "tazze":
        cucchiaini = numero * cucchiaini_per_tazza
    tazze = cucchiaini // cucchiaini_per_tazza
    cucchiaini = cucchiaini - tazze * cucchiaini_per_tazza
    cucchiai = cucchiaini // cucchiaini_per_cucchiai
    cucchiaini = cucchiaini - cucchiai * cucchiaini_per_cucchiai
    risultato = ""
    if tazze > 0:
        risultato = risultato + str(tazze) + "tazza"
        if tazze > 1:
            risultato = risultato + " tazze"
    if cucchiai > 0:
        if risultato != "":
            risultato = risultato + ", "

        risultato = risultato + str(cucchiai) + " cucchiaio"
        if cucchiai > 0:
            risultato = risultato + " cucchiai"
    if cucchiaini > 0:
        if risultato != "":
            risultato = risultato + ", "
        risultato = risultato + str(cucchiaini) + " cucchiaino"
        if cucchiaini > 1:
            risultato = risultato + " cucchiaini"
    if risultato == "":
        risultato = "0 cucchiai"
    return risultato

def main():
    print("59 Cucchiaini sono:", riduciMisura(59, "cucchiaini"))
    print("59 Cucchiai sono", riduciMisura(59, "cucchiai"))
    print("1 Cucchiaino sono:", riduciMisura(1, "cucchiaino"))
    print("1 Cucchiaio sono:", riduciMisura(1, "cucchiaio"))
    print("1 Tazza sono:", riduciMisura(1, "tazza"))
    print("4 Tazze sono:", riduciMisura(4, "tazze"))
    print("3 Cucchiaini sono:", riduciMisura(3, "cucchiaini"))
    print("6 Cucchiaini sono:", riduciMisura(6, "cucchiaini"))
    print("95 Cucchiaini sono:", riduciMisura(95, "cucchiaini"))
    print("96 Cucchiaini sono:", riduciMisura(96, "cucchiaini"))
    print("97 Cucchiaini sono:", riduciMisura(97, "cucchiaini"))
    print("98 Cucchiaini sono:", riduciMisura(98, "cucchiaini"))
    print("99 Cucchiaini sono:", riduciMisura(99, "cucchiaini"))

if __name__ == '__main__':
    main()
