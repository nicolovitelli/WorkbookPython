""" Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the level is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table. """
livello_suono = int(input("Inserisci, in Decibel, il livello del suono: "))
if livello_suono == 130:
    print("Jackhammer")
if livello_suono == 106:
    print("Gas Iawnmower")
if livello_suono == 70:
    print("Alarm Clock")
if livello_suono == 40:
    print("Quiet Room")
if livello_suono < 130 and livello_suono > 106:
    print("Livello del suono tra Jackhammer e Gas Iawnmover")
if livello_suono < 106 and livello_suono > 70:
    print("Livello del suono tra Gas Iawnmover e Alarm Clock")
if livello_suono < 70 and livello_suono > 40:
    print("Livello del suono tra Alarm Clock e Quiet Room")
if livello_suono < 40:
    print("Livello Suono minore di Quiet Room")
if livello_suono > 130:
    print("Livello Suono maggiore di Jackhammer")
