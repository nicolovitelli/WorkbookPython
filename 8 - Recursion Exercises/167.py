""" The notion of a palindrome was introduced previously in Exercise 72. In this exercise you will write a recursive
function that determines whether or not a string is a palindrome. The empty string is a palindrome,
as is any string containing only one character. Any longer string is a palindrome if its first and last characters
match, and if the string formed by removing the first and last characters is also a palindrome.
Write a main program that reads a string from the user. Use your recursive function
to determine whether or not the string is a palindrome. Then display an appropriate message for the user."""
def isPalindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[len(s) - 1] and isPalindrome(s[1 : len(s) - 1])

def main():
    line = input("Inserisci stringa: ")
    if isPalindrome(line):
        print("è un palindrome")
    else:
        print("non è un palindrome")

if __name__ == '__main__':
    main()
