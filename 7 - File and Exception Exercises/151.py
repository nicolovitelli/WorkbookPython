from random import randrange

""" While generating a password by selecting random characters generally gives a relatively secure password,
it also generally gives a password that is difficult to memorize.
As an alternative, some systems construct a password by taking two English words
and concatenating them. While this password isn’t as secure, it is much easier to
memorize. Write a program that reads a file containing a list of words, randomly selects two
of them, and concatenates them to produce a new password. When producing the
password ensure that the total length is between 8 and 10 characters, and that each
word used is at least three letters long. Capitalize each word in the password so that
the user can easily see where one word ends and the next one begins. Display the
password for the user. """
word_file = "../Data/words.txt"
words = []
inf = open(word_file, "r")
for line in inf:
    line = line.rstrip()
    if len(line) >= 3 and len(line) <= 7:
        words.append(line)
    inf.close()
    first = words[randrange(0, len(words))]
    first = first.capitalize()
    password = first
    while len(password) < 8 or len(password) > 10:
        second = words[randrange(0, len(words))]
        second = second.capitalize()
        password = first + second
    print("La Password casuale è:", password)
