""" The Sieve of Eratosthenes is a technique that was developed more than 2,000 years
ago to easily find all of the prime numbers between 2 and some limit, say 100. A
description of the algorithm follows:
Write down all of the numbers from 0 to the limit
Cross out 0 and 1 because they are not prime
Set p equal to 2
While p is less than the limit do
Cross out all multiples of p (but not p itself)
Set p equal to the next number in the list that is not crossed out
Report all of the numbers that have not been crossed out as prime """
def SieveOfEratosthenes(n):
    primo = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if primo[p] == True:
            for i in range(p * 2, n + 1, p):
                primo[i] = False
            p = p + 1
        primo[0] = False
        primo[1] = False
        for p in range(n + 1):
            if primo[p]:
                print(p)

def main():
    n = int(input("Inserisci Numero: "))
    print("Numeri primi sotto", n, "sono:")
    SieveOfEratosthenes(n)
    
if __name__ == '__main__':
    main()
