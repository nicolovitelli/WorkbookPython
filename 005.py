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
