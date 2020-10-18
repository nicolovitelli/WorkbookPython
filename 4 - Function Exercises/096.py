""" In this exercise you will write a function that determines whether or not a password
is good. We will define a good password to be a one that is at least 8 characters
long and contains at least one uppercase letter, at least one lowercase letter, and at
least one number. Your function should return true if the password passed to it as
its only parameter is good. Otherwise it should return false. Include a main program
that reads a password from the user and reports whether or not it is good. Ensure that your main program
only runs when your solution has not been imported into another file."""
def controllo_password(password):
    maiuscolo = False
    minuscolo = False
    numero = False
    if len(password) >= 8:
        for carattere in password:
            if carattere >= "A" and carattere <= "Z":
                maiuscolo = True
            elif carattere >= "a" and carattere <= "z":
                minuscolo = True
            elif carattere >= "0" and carattere <= "9":
                numero = True
        if maiuscolo and minuscolo and numero:
            print("Password sicura")
            return True
        else:
            print("Password non sicura: Carattere Maiuscolo, Minuscono o Numero mancante.")
    else:
        print("La Password non è lunga almeno 8 caratteri.")

def main():
    password = input("Inserisci Password: ")
    controllo_password(password)

if __name__ == '__main__':
    main()
