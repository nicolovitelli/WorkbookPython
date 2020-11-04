""" As the name implies, Roman numerals were developed in ancient Rome. Even after the Roman empire fell, its numerals
continued to be widely used in Europe until the late middle ages, and its numerals are still used in limited
circumstances today. Roman numerals are constructed from the letters M, D, C, L, X, V and I which represent 1000, 500,
100, 50, 5 and 1 respectively. Create a recursive function that converts a Roman numeral to an integer. Your function
should process one or two characters at the beginning of the string, and then call itself recursively on all of the 
unprocessed characters. Use an empty string, which has the value 0, for the base case. In addition, write a main
program that reads a Roman numeral from the user and displays its value. You can assume that the value entered by
the user is valid. Your program does not need to do any error checking. """
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1

def romanToDecimal(str):
    res = 0
    i = 0
    while (i < len(str)):
        # Getting value of symbol s[i]
        s1 = value(str[i])
        if (i + 1 < len(str)):
            # Getting value of symbol s[i + 1]
            s2 = value(str[i + 1])
            # Comparing both values
            if (s1 >= s2):
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
    return res

def main():
    # Driver code
    romano = input("inserisci numero romano: ")
    print("conversione in intero:", romanToDecimal(romano))

if __name__ == '__main__':
    main()
