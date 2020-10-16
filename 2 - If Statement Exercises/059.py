""" In a particular jurisdiction, older license plates consist of three uppercase letters
followed by three numbers. When all of the license plates following that pattern had been used,
the format was changed to four numbers followed by three uppercase letters.
Write a program that begins by reading a string of characters from the user. Then
your program should display a message indicating whether the characters are valid
for an older style license plate or a newer style license plate. Your program should
display an appropriate message if the string entered by the user is not valid for either
style of license plate."""
targa = input("Inserisci Targa: ")
if len(targa) == 6 and targa[0] >= "A" and targa[0] <= "Z" and\
    targa[1] >= "A" and targa[1] <= "Z" and \
    targa[2] >= "A" and targa[2] <= "Z" and \
    targa[3] >= "0" and targa[3] <= "9" and \
    targa[4] >= "0" and targa[4] <= "9" and \
    targa[5] >= "0" and targa[5] <= "9":
        print("La targa è del Vecchio Stile")
elif len(targa) == 7 and targa[0] >= "0" and targa[0] <= "9" and\
    targa[1] >= "0" and targa[1] <= "9" and \
    targa[2] >= "0" and targa[2] <= "9" and \
    targa[3] >= "0" and targa[3] <= "9" and \
    targa[4] >= "A" and targa[4] <= "Z" and \
    targa[5] >= "A" and targa[5] <= "Z" and \
    targa[6] >= "A" and targa[6] <= "Z":
        print("La targa è del Nuovo Stile")
else:
    print("Targa non valida")
