""" The novel “Gadsby” is over 50,000 words in length. While 50,000 words isn’t normally remarkable for a novel,
it is in this case because none of the words in the book use the letter “e”. This is particularly
noteworthy when one considers that “e” is the most common letter in English.
Write a program that reads a list of words from a file and determines what proportion of the words use each letter of
the alphabet. Display the result for all 26 letters. Include an additional message identifying the letter that is
used in the smallest proportion of the words. Your program should ignore any punctuation marks and
it should treat uppercase and lowercase letters as equivalent. """
word_file = "../Data/words.txt"
contains = {}
for ch in "ABCDEFGHILMNOPQRSTUVZ":
    contains[ch] = 0
num_words = 0
inf = open(word_file, "r")
for word in inf:
    word = word.upper().rstrip()
    unique = []
    for ch in word:
        if ch not in unique and ch != "-":
            unique.append(ch)
    for ch in unique:
        contains[ch] = contains[ch] + 1
    num_words = num_words + 1
inf.close()
smallest_count = min(contains.values())
for ch in sorted(contains):
    if contains[ch] == smallest_count:
        smallest_letter = ch
    percentage = contains[ch] / num_words * 100
    print(ch, "occurc in", percentage)
print()
print("Lettera", smallest_letter)
