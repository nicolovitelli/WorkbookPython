""" Two words are anagrams if they contain all of the same letters, but in a different
order. For example, “evil” and “live” are anagrams because each contains one e, one
i, one l, and one v. Create a program that reads two strings from the user, determines
whether or not they are anagrams, and reports the result. """
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
