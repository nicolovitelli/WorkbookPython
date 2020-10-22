""" While the popularity of cheques as a payment method has diminished in recent years,
some companies still issue them to pay employees or vendors. The amount being
paid normally appears on a cheque twice, with one occurrence written using digits,
and the other occurrence written using English words. Repeating the amount in two
different forms makes it much more difficult for an unscrupulous employee or vendor
to modify the amount on the cheque before depositing it.
In this exercise, your task is to create a function that takes an integer between 0 and
999 as its only parameter, and returns a string containing the English words for that
number. For example, if the parameter to the function is 142 then your function should
return “one hundred forty two”. Use one or more dictionaries to implement
your solution rather than large if/elif/else constructs. Include a main program that
reads an integer from the user and displays its value in English words. """
num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
            90: 'Ninety', 0: 'Zero'}

def n2w(n):
    try:
        print(num2words[n])
    except KeyError:
        try:
            print(num2words[n-n%10] + num2words[n%10].lower())
        except KeyError:
            print('Number out of range')

def main():
    num = int(input("Inserisci Numero: "))
    n2w(num)

if __name__ == '__main__':
    main()
    
    # funziona solo 1-99
