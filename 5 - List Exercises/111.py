""" In this exercise you will create a program that identifies all of the words in a string
entered by the user. Begin by writing a function that takes a string of text as its only
parameter. Your function should return a list of the words in the string with the punctuation
marks at the edges of the words removed. The punctuation marks that you must remove include commas, periods,
question marks, hyphens, apostrophes, exclamation points, colons, and semicolons.
Do not remove punctuation marks that appear in the middle of a words, such as the apostrophes used to
form a contraction. For example, if your function is provided with the string "Examples of contractions include:
don’t, isn’t, and wouldn’t." then your function should return the list ["Examples", "of", "contractions", "include",
"don’t", "isn’t", "and", "wouldn’t"]. Write a main program that demonstrates your function. It should read a string
from the user and display all of the words in the string with the punctuation marks
removed. You will need to import your solution to this exercise when completing
Exercise 158. As a result, you should ensure that your main program only runs when your file has not been
imported into another program."""
def divisione_parole(stringa):
    lista_parole = []
    somma_caratteri = ""
    for carattere in stringa:
        if carattere == "," or carattere == "!" or carattere == "?" or carattere == ":":
            pass
        elif carattere == " ":
            somma_caratteri = somma_caratteri + carattere
            lista_parole.append(somma_caratteri)
        else:
            somma_caratteri = somma_caratteri + carattere
    print(somma_caratteri)
    print(lista_parole)

def main():
    stringa = input("Inserisci Stringa: ")
    divisione_parole(stringa)

main()

# note: esercizio non completo, il programma registra nella lista solo la prima parola della stringa
