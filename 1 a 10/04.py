""" Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres. """
piedi_per_acro = 43560
lunghezza = float(input("Inserisci la Lunghezza: "))
larghezza = float(input("Inserisci la Larghezza: "))
acri = lunghezza * larghezza / piedi_per_acro
print("L'Area del Campo è di: ", acri, "acri")
