""" In the previous question you converted from note name to frequency. In this question
you will write a program that reverses that process. Begin by reading a frequency
from the user. If the frequency is within one Hertz of a value listed in the table in
the previous question then report the name of the note. Otherwise report that the
frequency does not correspond to a known note. In this exercise you only need to
consider the notes listed in the table. There is no need to consider notes from other
octaves. """
frequenza = float(input("Inserisci la Frequenza: "))
c4 = 261.63
d4 = 293.66
e4 = 329.63
f4 = 349.23
g4 = 392.00
a4 = 440.00
b4 = 493.88
if frequenza == c4:
    print("Nota: C4")
if frequenza == d4:
    print("Nota: D4")
if frequenza == e4:
    print("Nota: E4")
if frequenza == f4:
    print("Nota: F4")
if frequenza == g4:
    print("Nota: G4")
if frequenza == a4:
    print("Nota: A4")
if frequenza == b4:
    print("Nota: B4")
if frequenza > c4 and frequenza < d4:
    print("Nota: tra C4 e D4")
if frequenza > d4 and frequenza < e4:
    print("Nota: tra D4 e E4")
if frequenza > e4 and frequenza < f4:
    print("Nota: tra E4 e F4")
if frequenza > f4 and frequenza < g4:
    print("Nota: tra F4 e G4")
if frequenza > g4 and frequenza < a4:
    print("Nota: tra G4 e A4")
if frequenza > a4 and frequenza < b4:
    print("Nota: tra A4 e B4")
