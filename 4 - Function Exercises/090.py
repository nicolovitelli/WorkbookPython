""" In this exercise you will write a function named isInteger that determines
whether or not the characters in a string represent a valid integer. When determining
if a string represents an integer you should ignore any leading or trailing white space.
Once this white space is ignored, a string represents an integer if its length is at least
1 and it only contains digits, or if its first character is either + or - and the first
character is followed by one or more characters, all of which are digits.
Write a main program that reads a string from the user and reports whether or
not it represents an integer. Ensure that the main program will not run if the file
containing your solution is imported into another program. """
def isInteger(stringa):
    if "a" in stringa or "e" in stringa or "i" in stringa or "o" in stringa or "u" in stringa:
        print("Non hai inserito un Intero.")
    elif int(stringa)< 0 or int(stringa) > 0:
        print("Hai inserito un Intero.")

def main():
    stringa = input("Inserisci la Stringa: ")
    isInteger(stringa)

if __name__ == '__main__':
    main()
