""" A prime number is an integer greater than 1 that is only divisible by one and itself.
Write a function that determines whether or not its parameter is prime, returning
True if it is, and False otherwise. Write a main program that reads an integer
from the user and displays a message indicating whether or not it is prime. Ensure
that the main program will not run if the file containing your solution is imported
into another program. """
def numero_primo(numero):
    if numero > 1:
        for i in range(2, numero):
            if (numero % i) == 0:
                return False
        else:
            return True
    else:
        return False

def main():
    numero = int(input("Inserisci Numero: "))
    numero_primo(numero)

if __name__ == '__main__':
    main()
