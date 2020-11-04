""" Write a main program that reads a string from the user and uses your recursive function to determine
whether or not it is a palindrome. Then your program should display an appropriate message for the user. """
def isPalindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[len(s) - 1] and isPalindrome(s[1 : len(s) - 1])

def main():
    line = input("inserisci una stringa: ")
    if isPalindrome(line):
        print("palindromo")
    else:
        print("non un palindromo")

if __name__ == '__main__':
    main()
