""" Create a quare root function with two parameters. The first parameter, n, will be the number for which the square
root is being computed. The second parameter, guess, will be the current guess for the square foot. The guess parameter
should have a default value of 1.0. Do not provide a default value for the first parameter. Your square root function
will be recursive. The base can occuirs when guess^2 10^-12 is within on n. """
def goodEnough(guess, x):
    return abs((x - (guess * guess))) <= .01

def newGuess(guess, x):
    return (guess + guess/x)/2

def root(guess, x):
    if goodEnough(guess, x):
        return guess
    else:
        return root(newGuess(guess, x), x)

def sqrt(x):
    return root(x/2, x) #x/2 is usually somewhat close to the square root of a numbe

def main():
    n = int(input("inserisci il valore di n: "))
    sqrt(n)

if __name__ == '__main__':
    main()
