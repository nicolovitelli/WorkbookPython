""" Write a function that determines how many days there are in a particular month. Your
function will take two parameters: The month as an integer between 1 and 12, and
the year as a four digit integer. Ensure that your function reports the correct number
of days in February for leap years. Include a main program that reads a month and
year from the user and displays the number of days in that month. You may find your
solution to Exercise 57 helpful when solving this problem. """
def calcolo_giorni(mese, anno):
    if anno % 400 == 0 or anno % 4 == 0:
        if mese == 2:
            print("Giorni: 29")
        elif mese == 1 or mese == 3 or mese == 5 or mese == 7 or mese == 8 or mese == 10 or mese == 12:
            print("Giorni: 31")
        else:
            print("Giorni: 30")
    elif anno % 100 == 0:
        if mese == 2:
            print("Giorni: 28")
        elif mese == 1 or mese == 3 or mese == 5 or mese == 7 or mese == 8 or mese == 10 or mese == 12:
            print("Giorni: 31")
        else:
            print("Giorni: 30")
    else:
        if mese == 2:
            print("Giorni: 28")
        elif mese == 1 or mese == 3 or mese == 5 or mese == 7 or mese == 8 or mese == 10 or mese == 12:
            print("Giorni: 31")
        else:
            print("Giorni: 30")

def main():
    mese = int(input("Inserisci Mese: "))
    anno = int(input("Inserisci Anno: "))
    calcolo_giorni(mese, anno)

if __name__ == '__main__':
    main()
