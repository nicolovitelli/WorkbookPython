""" Exercise 51 included a table that shows the conversion from letter grades to grade
points at a particular academic institution. In this exercise you will compute the
grade point average of an arbitrary number of letter grades entered by the user. The
user will enter a blank line to indicate that all of the grades have been provided. For
example, if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.
You may find your solution to Exercise 51 helpful when completing this exercise.
Your program does not need to do any error checking. It can assume that each value
entered by the user will always be a valid letter grade or a blank line. """
riga = input("Inserisci Valutazione in Lettere: ")
punteggio = 0.0
media = []
m = 0
def mediaLista(lista):
    return sum(lista) / len(lista)
while riga != "":
    lettera = riga
    if lettera == "A+":
        punteggio = 4.0
    elif lettera == "A":
        punteggio = 4.0
    elif lettera == "A-":
        punteggio = 3.7
    elif lettera == "B+":
        punteggio = 3.3
    elif lettera == "B":
        punteggio = 3.0
    elif lettera == "B-":
        punteggio = 2.7
    elif lettera == "C+":
        punteggio = 2.3
    elif lettera == "C":
        punteggio = 2.0
    elif lettera == "C-":
        punteggio = 1.7
    elif lettera == "D+":
        punteggio = 1.3
    elif lettera == "D":
        punteggio = 1.0
    elif lettera == "F":
        punteggio = 0.0
    media.append(punteggio)
    m = mediaLista(media)
    riga = input("Inserisci Valutazione in Lettere: ")
print("Media dei Voti:", round(m, 2))
