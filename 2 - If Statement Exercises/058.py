""" Write a program that reads a date from the user and computes its immediate successor.
For example, if the user enters values that represent 2013-11-18 then your program
should display a message indicating that the day immediately after 2013-11-18 is
2013-11-19. If the user enters values that represent 2013-11-30 then the program
should indicate that the next day is 2013-12-01. If the user enters values that represent
2013-12-31 then the program should indicate that the next day is 2014-01-01. The
date will be entered in numeric form with three separate input statements; one for
the year, one for the month, and one for the day. Ensure that your program works
correctly for leap years. """
anno = int(input("Inserisci Anno: "))
mese = int(input("Inserisci Mese: "))
giorno = int(input("Inserisci Giorno: "))
bisestile = True
if anno % 400 == 0:
    bisestile = True
elif anno % 100 == 0:
    bisestile = False
elif anno % 4 == 0:
    bisestile = True
else:
    bisestile = False
if bisestile == True:
    if mese == 10 or mese == 12 or mese == 8 or mese == 7 or mese == 5 or mese == 3 or mese == 1:
        if giorno == 31 and mese != 12:
            mese += 1
            giorno = 1
            print("Giorno Successivo (AAAA-M-G):", anno, "-", mese, "-", giorno)
        elif mese == 12 and giorno == 31:
            mese = 1
            giorno = 1
            anno += 1
            print("Giorno Successivo (AAAA-M-G):", anno, "-", mese, "-", giorno)
        else:
            giorno += 1
            print("Giorno Successivo (AAAA-M-G):", anno, "-", mese, "-", giorno)
    elif mese == 4 or mese == 6 or mese == 9 or mese == 11:
        if giorno == 31 and mese != 12:
            mese += 1
            giorno = 1
            print("Giorno Successivo (AAAA-M-G):", anno, "-", mese, "-", giorno)
        else:
            giorno += 1
            print("Giorno Successivo (AAAA-M-G):", anno, "-", mese, "-", giorno)
    elif mese == 2 and giorno == 29:
        mese = 3
        giorno = 1
        print("Giorno Successivo (AAAA-M-G):", anno, "-", mese, "-", giorno)
if bisestile == False:
    if mese == 2:
        mese += 1
        giorno = 1
        print("Giorno Successivo (AAAA-M-G):", anno, "-", mese, "-", giorno)
    elif mese == 10 or mese == 12 or mese == 8 or mese == 7 or mese == 5 or mese == 3 or mese == 1:
        if giorno == 31 and mese != 12:
            mese += 1
            giorno = 1
            print("Giorno Successivo (AAAA-M-G):", anno, "-", mese, "-", giorno)
        elif mese == 12:
            if giorno == 31:
                mese = 1
                giorno = 1
                anno += 1
                print("Giorno Successivo (AAAA-M-G):", anno, "-", mese, "-", giorno)
        else:
            giorno += 1
            print("Giorno Successivo (AAAA-M-G):", anno, "-", mese, "-", giorno)
