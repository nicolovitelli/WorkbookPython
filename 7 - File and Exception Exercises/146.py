""" One technique that can be used to help break some simple forms of encryption is
frequency analysis. This analysis examines the encrypted text to determine which
characters are most common. Then it tries to map the most common letters in English,
such as E and T, to the most commonly occurring characters in the encrypted
text. Write a program that initiates this process by determining and displaying the
frequencies of all letters in a file. Ignore spaces, punctuation marks, and numbers as
you perform this analysis. Your program should be case insensitive, treating a and
A as equivalent. The user will provide the file name as a command line parameter.
Your program should display a meaningful error message if the user provides the
wrong number of command line parameters, or if the program is unable to open the
file indicated by the user. """
def frequenzaLettere(file):
    with open(file) as f:
        c = Counter()
        for line in f:
            c = c + Counter(line)

def main():
    nomefile = input("Inserisci Nome del FIle: ")
    frequenzaLettere(nomefile)

if __name__ == '__main__':
    main()
