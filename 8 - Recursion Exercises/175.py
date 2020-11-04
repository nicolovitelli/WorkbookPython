""" In Exercise 82 you wrote a program that used a loop to convert a decimal number to its binary 
representation. In this exercise you will perform the same task using recursion. Write a recursive function that
converts a non-negative decimal number to binary. Treat 0 and 1 as base cases which return a string containing the
appropriate digit. For all other positive integers, n, you should compute the next digit using the remainder operator
and then make a recursive call to compute the digits of n / 2 """
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
def main():
    dec = int(input("inserisci numero decimale: "))
    convertToBinary(dec)

if __name__ == '__main__':
    main()
