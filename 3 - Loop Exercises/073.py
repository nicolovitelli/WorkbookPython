""" There are numerous phrases that are palindromes when spacing is ignored. Examples
include “go dog”, “flee to me remote elf” and “some men interpret nine memos”,
among many others. Extend your solution to Exercise 72 so that it ignores spacing
while determining whether or not a string is a palindrome. For an additional challenge,
extend your solution so that is also ignores punctuation marks and treats uppercase
and lowercase letters as equivalent. """
frase = input("Inserisci una Frase: ")
palindromo = True
for i in range(0, len(frase) // 2):
    if frase[i] != frase[len(frase) - i - 1]:
        palindromo = False
    if palindromo:
        print(frase, "è palindromo")
    else:
        print(frase, "non è palindromo")
       
