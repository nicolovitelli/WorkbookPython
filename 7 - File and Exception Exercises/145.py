""" In this exercise you will create a Python program that identifies the longest word(s)
in a file. Your program should output an appropriate message that includes the length
of the longest word, along with all of the words of that length that occurred in the
file. Treat any group of non-white space characters as a word, even if it includes
numbers or punctuation marks. """
def longest_word(nomefile):
    with open(nomefile, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

def main():
    nomefile = input("Inserisci Nome File: ")
    print(longest_word(nomefile))

if __name__ == '__main__':
    main()
