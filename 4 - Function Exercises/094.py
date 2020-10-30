from random import randint

""" Write a function that generates a random password. The password should have a
random length of between 7 and 10 characters. Each character should be randomly
selected from positions 33 to 126 in the ASCII table. Your function will not take
any parameters. It will return the randomly generated password as its only result.
Display the randomly generated password in your file’s main program. Your main
program should only run when your solution has not been imported into another file. """
def password_random():
    lunghezza = randint(7, 10)
    risultato = ""
    for i in range(lunghezza):
        carattere_casuale = chr(randint(33, 126))
        risultato = risultato + carattere_casuale
    return risultato

def main():
    print("Password Casuale:", password_random())

if __name__ == '__main__':
    main()
