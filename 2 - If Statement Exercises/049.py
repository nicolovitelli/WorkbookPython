""" The following table contains earthquake magnitude ranges on the Richter scale and
their descriptors: Write a program that reads a magnitude from the user and displays the appropriate
descriptor as part of a meaningful message. For example, if the user enters 5.5 then
your program should indicate that a magnitude 5.5 earthquake is considered to be a
moderate earthquake. """
magnitudo = float(input("Inserisci il Magnitudo: "))
if magnitudo < 2.0:
    print("Micro")
elif magnitudo > 2.0 and magnitudo < 3.0:
    print("Very minor")
elif magnitudo > 3.0 and magnitudo < 4.0:
    print("Minor")
elif magnitudo > 4.0 and magnitudo < 5.0:
    print("Light")
elif magnitudo > 5.0 and magnitudo < 6.0:
    print("Moderate")
elif magnitudo > 6.0 and magnitudo < 7.0:
    print("Strong")
elif magnitudo > 7.0 and magnitudo < 8.0:
    print("Major")
elif magnitudo > 8.0 and magnitudo < 10.0:
    print("Great")
elif magnitudo > 10.0:
    print("Meteoric")
