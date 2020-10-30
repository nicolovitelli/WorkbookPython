from sys import argv

""" A spell checker can be a helpful tool for people who struggle to spell words correctly.
In this exercise, you will write a program that reads a file and displays all of the words
in it that are misspelled. Misspelled words will be identified by checking each word
in the file against a list of known words. Any words in the user’s file that do not
appear in the list of known words will be reported as spelling mistakes.
The user will provide the name of the file to check for spelling mistakes as a
command line parameter. Your program should display an appropriate error message
if the command line parameter is missing. An error message should also be displayed
if your program is unable to open the user’s file. Use your solution to Exercise 111
when creating your solution to this exercise so that words followed by a comma,
period or other punctuation mark are not reported as spelling mistakes. Ignore the
capitalization of the words when checking their spelling. """
words_file = "../Data/words.txt"
if len(argv) != 2:
    print("Inserisci almeno un comando:")
    quit()
try:
    inf = open(argv[1], "r")
except:
    print("Errore")
    quit()
valid = {}
words_file = open(words_file, "r")
for word in words_file:
    word = word.lower().rstrip()
    valid[word] = 0
words_file.close()

misspelled = []
for line in inf:
    words = onlyTheWords(line)
    for word in words:
        if word.lower() not in valid and word not in misspelled:
            misspelled.append(word)
inf.close()
if len(misspelled) == 0:
    print("non ci sono parole")
else:
    print("parole:")
    for word in misspelled:
        print(" ", word)
