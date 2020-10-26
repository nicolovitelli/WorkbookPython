""" Create a program that sums all of the numbers entered by the user while ignoring
any lines entered by the user that are not valid numbers. Your program should display
the current sum after each number is entered. It should display an appropriate
error message after any invalid input, and then continue to sum any additional numbers
entered by the user. Your program should exit when the user enters a blank
line. Ensure that your program works correctly for both integers and floating point numbers. """
line = input("Inserisci un numero: ")
totale = 0
while line != "":
    try:
        num = float(line)
        totale = totale + num
        print("Totale:" , totale)
    except ValueError:
        print("Non era un numero")
        line = input("Inserisci un Numero: ")
print("Totale:", totale)
