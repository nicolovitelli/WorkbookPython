""" In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant. """
lettera = input("Inserisci la lettera: ")
if lettera == "a" or lettera == "e" or lettera == "i" or lettera == "o" or lettera == "u":
    print("la Lettera che hai inserito è una vocale.")
elif lettera == "y":
    print("a volte la lettera Y è una vocale, a volte una consonante.")
else:
    print("la Lettera che hai inserito è una consonante.")
