""" An integer, n, is said to be perfect when the sum of all of the proper divisors of n is
equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2,
4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.
Write a function that determines whether or not a positive integer is perfect. Your
function will take one parameter. If that parameter is a perfect number then your function will return true.
Otherwise it will return false. In addition, write a main program that uses your function to identify
and display all of the perfect numbers between 1 and 10,000.
Import your solution to Exercise 109 when completing this task. """
limite = 10000

def numero_perfetto(n):
    divisori = trova_divisori(n)
    totale = 0
    for d in divisori:
        totale = totale + d
    if totale == n:
        return True
    else:
        return False

def main():
    print("Numeri Perfetti tra 1 e", limite, "sono:")
    for i in range(1, limite + 1):
        if numero_perfetto(i):
            print(" ", i)

main()
