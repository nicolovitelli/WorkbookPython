""" The notion of anagrams can be extended to multiple words. For example, “William
Shakespeare” and “I am a weakish speller” are anagrams when capitalization and
spacing are ignored. Extend your program from Exercise 135 so that it is able to check if two phrases
are anagrams. Your program should ignore capitalization, punctuation marks and
spacing when making the determination. """
def contaCaratteri(s):
    contatori = {}
    for ch in s:
        if ch in contatori:
            contatori[ch] = contatori[ch] + 1
        else:
            contatori[ch] = 1
    return contatori

def main():
    s1 = input("Inserisci la Prima Stringa: ")
    s2 = input("Inserisci la Seconda Stringa: ")
    contatori1 = contaCaratteri(s1)
    contatori2 = contaCaratteri(s2)
    if contatori1 == contatori2:
        print("Anagramma")
    else:
        print("Non è un Anagramma")

if __name__ == '__main__':
    main()
    
    # esercizio non completo 
