""" Spelling mistakes are only one of many different kinds of errors that might appear in
a written work. Another error that is common for some writers is a repeated word. For
example, an author might inadvertently duplicate a word, as shown in the following
sentence: Some word processors will detect this error and identify it when a spelling or grammar
check is performed. """
words_file = "../Data/words.txt"
words_file.split()
seen = set()
dups = set()
for word in words_file:
    if word in seen:
        if word not in dups:
            print(word)
            dups.add(word)
    else:
        seen.add(word)
print(seen, dups)
