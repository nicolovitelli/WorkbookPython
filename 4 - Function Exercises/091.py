""" Write a function named precedence that returns an integer representing the precedence of a mathematical operator.
A string containing the operator will be passed to the function as its only parameter.
Your function should return 1 for + and -, 2 for * and /, and 3 for ˆ. If the string passed to the function
is not one of these operators then the function should return -1. Include a main program that reads an operator
from the user and either displays the operator’s precedence or an error message indicating that the input was not
an operator. Your main program should only run when the file containing your solution has not been imported into
another program. """
def precedence(stringa):
    if stringa == "+" or stringa == "-":
        print("Precedenza dell'Operatore:")
        return "1"
    elif stringa == "*" or stringa == "/":
        print("Precedenza dell'Operatore:")
        return "2"
    elif stringa == "^":
        print("Precedenza dell'Operatore:")
        return "3"
    else:
        return "-1"

def main():
    operatore = input("Inserisci Operatore: ")
    precedence(operatore)

if __name__ == '__main__':
    main()
