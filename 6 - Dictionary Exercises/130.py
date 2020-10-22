""" On some basic cell phones, text messages can be sent using the numeric keypad.
Because each key has multiple letters associated with it, multiple key presses are
needed for most letters. Pressing the number once generates the first letter on the
key. Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth
character listed for that key. """
def tasti_telefono():
    tasti_numeri = {
    '1':['.',',','?','!',':'],
    '2':['A' or 'a','B' or 'b','C' or 'c'],
    '3':['D' or 'd','E' or 'e','F' or 'f'],
    '4':['G' or 'g','H' or 'h','I' or 'i'],
    '5':['J' or 'j','K' or 'k','L' or 'l'],
    '6':['M' or 'm','N' or 'n','O' or 'o'],
    '7':['P' or 'p','Q' or 'q','R' or 'r','S' or 's'],
    '8':['T' or 't','U' or 'u','V' or 'v'],
    '9':['W' or 'w','X' or 'x','Y' or 'y','Z' or 'z'],
    '0':[' '] }

    testo = list(input("Inserisci un Testo: "))
    
    # non completo
