""" Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below: Write a program that reads
the frequency of the radiation from the user and displays the appropriate name."""
frequenza = int(input("Inserisci Frequenza: "))
if frequenza < 3 * (10 ** 9):
    print("Onde Radio")
elif frequenza > 3 * (10 ** 9) and frequenza < 3 * (10 ** 12):
    print("Micro Onde")
elif frequenza > 3 * (10 ** 12) and frequenza < 4.3 * (10 ** 14):
    print("Luce Infrarossa")
elif frequenza > 4.3 * (10 ** 14) and frequenza < 7.5 * (10 ** 14):
    print("Luce Visibile")
elif frequenza > 7.5 * (10 ** 14) and frequenza < 3 * (10 ** 17):
    print("Raggi Ultravioletti")
elif frequenza > 3 * (10 ** 17) and frequenza < 3 * (10 ** 19):
    print("Raggi X")
elif frequenza > 3 * (10 ** 19):
    print("Raggi Gamma")
else:
    print("Frequenza Non Valida")
