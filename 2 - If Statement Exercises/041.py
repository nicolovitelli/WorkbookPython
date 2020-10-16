""" Begin by writing a program that reads the name of a note from the user and
displays the note’s frequency. Your program should support all of the notes listed
previously.
Once you have your program working correctly for the notes listed previously you
should add support for all of the notes from C0 to C8. While this could be done by
adding many additional cases to your if statement, such a solution is cumbersome,
inelegant and unacceptable for the purposes of this exercise. Instead, you should
exploit the relationship between notes in adjacent octaves. In particular, the frequency
of any note in octave n is half the frequency of the corresponding note in octave n+1.
By using this relationship, you should be able to add support for the additional notes
without adding additional cases to your if statement. """
nota = input("Inserisci nota: ")
c4 = 261.63
d4 = 293.66
e4 = 329.63
f4 = 349.23
g4 = 392.00
a4 = 440.00
b4 = 493.88
nome_nota = nota[0]
numero_nota = int(nota[1])
if nome_nota == "C":
    frequenza = c4
elif nome_nota == "D":
    frequenza = d4
elif nome_nota == "E":
    frequenza = e4
elif nome_nota == "F":
    frequenza = f4
elif nome_nota == "G":
    frequenza = g4
elif nome_nota == "A":
    frequenza = a4
elif nome_nota == "B":
    frequenza = b4
frequenza = frequenza / 2 ** (4 - numero_nota)
print("La frequenza di", nome_nota, "è:", frequenza)
