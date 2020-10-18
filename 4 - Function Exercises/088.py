""" If you have 3 straws, possibly of differing lengths, it may or may not be possible
to lay them down so that they form a triangle when their ends are touching. For
example, if all of the straws have a length of 6 inches. then one can easily construct
an equilateral triangle using them. However, if one straw is 6 inches. long, while the
other two are each only 2 inches. long, then a triangle cannot be formed. In general,
if any one length is greater than or equal to the sum of the other two then the lengths
cannot be used to form a triangle. Otherwise they can form a triangle.
Write a function that determines whether or not three lengths can form a triangle.
The function will take 3 parameters and return a Boolean result. In addition, write a
program that reads 3 lengths from the user and demonstrates the behaviour of this
function. """
def se_triangolo(lato1, lato2, lato3):
    if lato1 >= (lato2 + lato3):
        return False
    elif lato2 >= (lato1 + lato3):
        return False
    elif lato3 >= (lato1 + lato2):
        return False
    else:
        return True

def dimostrazione_triangolo():
    lato1 = float(input("Inserisci Lato1: "))
    lato2 = float(input("Inserisci Lato2: "))
    lato3 = float(input("Inserisci Lato3: "))
    se_triangolo(lato1, lato2, lato3)

dimostrazione_triangolo()
