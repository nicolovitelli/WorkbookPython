""" A magic date is a date where the day multiplied by the month is equal to the two digit
year. For example, June 10, 1960 is a magic date because June is the sixth month, and
6 times 10 is 60, which is equal to the two digit year. Write a function that determines
whether or not a date is a magic date. Use your function to create a main program
that finds and displays all of the magic dates in the 20th century. You will probably
find your solution to Exercise 100 helpful when completing this exercise. """
def data_magica(giorno, mese, anno):
    if giorno * mese == anno % 100:
        return True
    return False

def main():
    for year in range(1900, 2000):
        for month in range(1, 13):
            for day in range(1, calcolo_giorni(mese, anno) + 1):
                if data_magica(giorno, mese, anno):
                    print("E' una Data Magica.")

if __name__ == '__main__':
    main()
