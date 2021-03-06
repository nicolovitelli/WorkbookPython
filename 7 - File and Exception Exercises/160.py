""" Sensitive information is often removed, or redacted, from documents before they
are released to the public. When the documents are released it is common for the
redacted text to be replaced with black bars.
In this exercise you will write a program that redacts all occurrences of sensitive
words in a text file by replacing them with asterisks. Your program should redact
sensitive words wherever they occur, even if they occur in the middle of another
word. The list of sensitive words will be provided in a separate text file. Save the
redacted version of the original text in a new file. The names of the original text file,
sensitive words file, and redacted file will all be provided by the user. """
inf_name = input("inserisci nome file: ")
inf = open(inf_name, "r")
sen_name = input("inserisci nome file parole sensititive:")
sen = open(sen_name, "r")
words = []
line = sen.readline()
while line != "":
    line = line.rstrip()
    words.append(line)
    
    line = sen.readline()
sen.close()
outf_name = input("inserisci nome nuovo file: ")
outf = open(outf_name, "w")
line = inf.readline()
while line != "":
    for word in words:
        line = line.replace(word, "*" * len(word))
    outf.write(line)
    line = inf.readline()
inf.close()
outf.close()
