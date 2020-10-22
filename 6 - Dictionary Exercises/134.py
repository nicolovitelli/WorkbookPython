""" Create a program that determines and displays the number of unique characters in a
string entered by the user. For example, Hello, World! has 10 unique characters
whilezzzhas only one unique character. Use a dictionary or set to solve this problem. """
s = input("Inserisci una Stringa: ")
caratteri = {}
for ch in s:
    caratteri[ch] = True
print("La stringa contiene:", len(caratteri), "caratteri")
