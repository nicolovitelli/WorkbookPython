""" A string is a palindrome if it is identical forward and backward. For example “anna”,
“civic”, “level” and “hannah” are all examples of palindromic words.Write a program
that reads a string from the user and uses a loop to determines whether or not it is a
palindrome. Display the result, including a meaningful output message. """
stringa = input("Inserisci una Stringa: ")
palindromo = True
for i in range(0, len(stringa) // 2):
    if stringa[i] != stringa[len(stringa) - i - 1]:
        palindromo = False
if palindromo:
    print(stringa, "è palindromo")
else:
    print(stringa, "non è palindromo")
