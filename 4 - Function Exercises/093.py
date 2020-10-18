""" In this exercise you will create a function named nextPrime that finds and returns
the first prime number larger than some integer, n. The value of n will be passed to 
the function as its only parameter. Include a main program that reads an integer from
the user and displays the first prime number larger than the entered value. Import
and use your solution to Exercise 92 while completing this exercise. """
def numero_primo(numero):
    if (numero <= 1):
        return False
    if (numero <= 3):
        return True
    if (numero % 2 == 0 or numero % 3 == 0):
        return False
    for i in range(5, int(math.sqrt(numero) + 1), 6):
        if (numero % i == 0 or numero % (i + 2) == 0):
            return False
    return True

def nextPrime(altro_num):
    if (altro_num <= 1):
        return 2
    primo = altro_num
    trovato = False
    while (not trovato):
        primo = primo + 1
        if (numero_primo(primo) == True):
            trovato = True
    return primo

altro_num = int(input("Inserisci la grandezza massima per la ricerca del prossimo numero primo: "))
print("Numero Primo dopo", altro_num, "è", nextPrime(altro_num))
