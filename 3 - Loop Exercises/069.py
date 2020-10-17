""" The value of π can be approximated by the following infinite series:
Write a program that displays 15 approximations of π. The first approximation
should make use of only the first term from the infinite series.
Each additional approximation displayed by your program should include one more term in the series, making
it a better approximation of π than any of the approximations displayed previously"""
prima_cifra = 2
seconda_cifra = 3
terza_cifra = 4
for numero in range(16):
    pi = 3 + (4 / prima_cifra * seconda_cifra * terza_cifra)
    prima_cifra = prima_cifra + 2
    seconda_cifra = seconda_cifra + 2
    terza_cifra = terza_cifra + 2
    print(pi)
