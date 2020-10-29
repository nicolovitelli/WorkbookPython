""" Euclid was a Greek mathematician who lived approximately 2,300 years ago. His
algorithm for computing the greatest common divisor of two positive integers, a and
b, is both efficient and recursive. It is outlined below:
If b is 0 then Return a Else
Set c equal to the remainder when a is divided by b
Return the greatest common divisor of b and c
Write a program that implements Euclid’s algorithm and uses it to determine the
greatest common divisor of two integers entered by the user. """
def algoritmoEuclide(b, a):
    if b == 0:
        return a
    else:
        c = a % b
        while b != 0:
            c, b = c, b%c
        return c

def main():
    b = int(input("inserisci B: "))
    a = int(input("inserisci A: "))
    algoritmoEuclide(b, a)

if __name__ == '__main__':
    main()
