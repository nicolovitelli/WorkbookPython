import math
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
