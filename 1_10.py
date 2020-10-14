# ESERCIZIO 1
""" Create a program that displays your name and complete mailing address formatted in
the manner that you would usually see it on the outside of an envelope. Your program
does not need to read any input from the user. """
print("Nicolò Vitelli")
print("Via delle Pesche 10")
print("Albano Laziale - 00041")
print("Roma (RM)")

# ESERCIZIO 2
""" Write a program that asks the user to enter his or her name. The program should
respond with a message that says hello to the user, using his or her name. """
nome = input("Inserisci il tuo Nome: ")
print("Benvenuto " + nome)

# ESERCIZIO 3
""" Write a program that asks the user to enter the width and length of a room. Once
the values have been read, your program should compute and display the area of the
room. The length and the width will be entered as floating point numbers. Include
units in your prompt and output message; either feet or meters, depending on which
unit you are more comfortable working with. """
l = input("Inserisci la Larghezza: ")
l1 = input("Inserisci la Lunghezza: ")
larghezza = float(l)
lunghezza = float(l1)
area = larghezza * lunghezza
print(area)

# ESERCIZIO 4
""" Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres. """
piedi_per_acro = 43560
lunghezza = float(input("Inserisci la Lunghezza: "))
larghezza = float(input("Inserisci la Larghezza: "))
acri = lunghezza * larghezza / piedi_per_acro
print("L'Area del Campo è di: ", acri, "acri")

# ESERCIZIO 5
""" In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places. """
deposito_minore = 0.10
deposito_maggiore = 0.25
minore = int(input("Quanti contenitori da 1 Litro o meno hai? "))
maggiore = int(input("Quanti contenitori da più di 1 Litro hai? "))
rimborso = minore * deposito_minore + maggiore * deposito_maggiore
print("Hai accumulato un rimborso pari a: $", rimborso)

# ESERCIZIO 6
""" The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places. """
piatto = float(input("Inserisci il costo del piatto ordinato: "))
tasse = (piatto * 22) / 100
mancia = (piatto * 18) / 100
totale = piatto + tasse + mancia
print("Il costo totale del piatto è di: $", totale)
print("Compreso di Tasse: $", tasse, "e Mancia: $", mancia)

# ESERCIZIO 7
""" Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula: sum = (n)(n + 1) / 2"""
n = int(input("Inserisci il Numero: "))
somma = n * (n+1) / 2
print("La somma di", n, "agli interi positivi è:", somma)

# ESERCIZIO 8
""" An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order. """
peso_widget = 75 # grammi
peso_gizmo = 112 # grammi
widget = int(input("Inserisci il numero di Widget: "))
gizmo = int(input("Inserisci il numero di Gizmo: "))
tot_widget = widget * peso_widget
tot_gizmo = gizmo * peso_gizmo
print("Peso totale ordine:", tot_gizmo + tot_widget, "grammi")

# ESERCIZIO 9
""" Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places. """
interessi_per_anno = 4 # %
deposito = float(input("Inserisci la quantità di soldi depositati nell'account: "))
primo_anno = (deposito * interessi_per_anno) / 100
secondo_anno = (deposito * (interessi_per_anno * 2)) / 100
terzo_anno = (deposito * (interessi_per_anno * 3)) / 100
print("Totale Interessi dopo il primo anno: %.2f$" % primo_anno)
totale_anno1 = deposito + primo_anno
print("-> per un totale di: %.2f$" % totale_anno1)
print("Totale Interessi dopo il secondo anno: %.2f$" % secondo_anno)
totale_anno2 = deposito + secondo_anno
print("-> per un totale di: %.2f$" % totale_anno2)
print("Totale Interessi dopo il terzo anno: %.2f$" % terzo_anno)
totale_anno3 = deposito + terzo_anno
print("-> per un totale di: %.2f$" % totale_anno3)

# ESERCIZIO 10
""" Create a program that reads two integers, a and b, from the user. Your program should
compute and display:
• The sum of a and b
• The difference when b is subtracted from a
• The product of a and b 
• The quotient when a is divided by b
• The remainder when a is divided by b
• The result of log10 a
• The result of ab """
a = int(input("Inserisci il valore di A: "))
b = int(input("Inserisci il valore di B: "))
somma = a + b
sottrazione = a - b
prodotto = a * b
quoziente = a / b
resto = a % b
print(a, "+", b, "=", somma)
print(a, "-", b, "=", sottrazione)
print(a, "*", b, "=", prodotto)
print(a, "/", b, "=", quoziente, "con resto di", resto)
print("Logaritmo in base 10 di", a, "=", log10(a))
print(a, "^", b, "=", a**b)
