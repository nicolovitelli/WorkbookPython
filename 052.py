""" In the previous exercise you created a program that converts a letter grade into the
equivalent number of grade points. In this exercise you will create a program that
reverses the process and converts from a grade point value entered by the user to a
letter grade. Ensure that your program handles grade point values that fall between
letter grades. These should be rounded to the closest letter grade. Your program
should report A+ for a 4.0 (or greater) grade point average. """
grado = float(input("Inserisci Grado: "))
if grado > 4.0:
    print("Lettera: A+")
elif grado == 4.0:
    print("Lettera: A")
elif grado < 4.0 and grado >= 3.7:
    print("Lettera: A-")
elif grado < 3.7 and grado >= 3.3:
    print("Lettera: B+")
elif grado < 3.3 and grado >= 3.0:
    print("Lettera: B")
elif grado < 3.0 and grado >= 2.7:
    print("Lettera: B-")
elif grado < 2.7 and grado >= 2.3:
    print("Lettera: C+")
elif grado < 2.3 and grado >= 2.0:
    print("Lettera: C")
elif grado < 2.0 and grado >= 1.7:
    print("Lettera: C-")
elif grado < 1.7 and grado >= 1.3:
    print("Lettera: D+")
elif grado < 1.3 and grado >= 1.0:
    print("Lettera: D")
elif grado < 1.0:
    print("Lettera: F")
