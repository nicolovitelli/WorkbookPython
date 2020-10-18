""" The Twelve Days of Christmas is a repetitive song that describes an increasingly
long list of gifts sent to one’s true love on each of 12 days. A single gift is sent on
the first day. A new gift is added to the collection on each additional day, and then
the complete collection is sent. The first three verses of the song are shown below.
The complete lyrics are available on the internet. Your task is to write a program
that displays the complete lyrics for The Twelve
Days of Christmas. Write a function that takes the verse number as its only parameter
and displays the specified verse of the song. Then call that function 12 times with
integers that increase from 1 to 12. Each item that is sent to the recipient in the song
should only appear once in your program, with the possible exception of the partridge.
It may appear twice if that helps you handle the difference between “A partridge in a pear tree”
in the first verse and “And a partridge in a pear tree” in the subsequent verses.
Import your solution to Exercise 85 to help you complete this exercise. """
def dodici_giorni_natale(verso):
    verso_1 = "On the first day of Christmas my true love sent to me\nA partridge in a pear tree\n"
    verso_2 = "On the second day of Christmas my true love sent to me\n" \
              "Two turtle doves, and\nA partridge in a pear tree\n"
    verso_3 = "On the third day of Christmas my true love sent to me\nThree french hens\n" \
              "Two turtle doves, and\nA partridge in a pear tree\n"
    verso_4 = "On the fourth day of Christmas my true love sent to me\nFour calling birds\nThree french hens\n" \
              "Two turtle doves, and\nA partridge in a pear tree\n"
    verso_5 = "On the fifth day of Christmas my true love sent to me\nFive golden rings\nFour calling birds\n" \
              "Three french hens\nTwo turtle doves, and\nA partridge in a pear tree\n"
    verso_6 = "On the sixth day of Christmas my true love sent to me\nSix geese a-laying\nFive golden rings\n" \
              "Four calling birds\nThree french hens\nTwo turtle doves, and\nA partridge in a pear tree\n"
    verso_7 = "On the seventh day of Christmas my true love sent to me\nSeven swans a-swimming\n" \
              "Six geese a-laying\nFive golden rings\nFour calling birds\nThree french hens\nTwo turtle doves, and\n" \
              "A partridge in a pear tree\n"
    verso_8 = "On the eighth day of Christmas my true love sent to me\nEight maids a-milking\nSeven swans a-swimming\n" \
              "Six geese a-laying\nFive golden rings\nFour calling birds\nThree french hens\nTwo turtle doves, and\n" \
              "A partridge in a pear tree\n"
    verso_9 = "On the ninth day of Christmas my true love sent to me\nNine ladies dancing\nEight maids a-milking\n" \
              "Seven swans a-swimming\nSix geese a-laying\nFive golden rings\nFour calling birds\nThree french hens\n" \
              "Two turtle doves, and\nA partridge in a pear tree\n"
    verso_10 = "On the 10th day of Christmas my true love sent to me\n10 lords a-leaping\nNine ladies dancing\n" \
               "Eight maids a-milking\nSeven swans a-swimming\nSix geese a-laying\nFive golden rings\n" \
               "Four calling birds\nThree french hens\nTwo turtle doves, and\nA partridge in a pear tree\n"
    verso_11 = "On the 11th day of Christmas my true love sent to me\n11 pipers piping\n10 lords a-leaping\n" \
               "Nine ladies dancing\nEight maids a-milking\nSeven swans a-swimming\nSix geese a-laying\n" \
               "Five golden rings\nFour calling birds\nThree french hens\nTwo turtle doves, and\n" \
               "A partridge in a pear tree\n"
    verso_12 = "On the 12th day of Christmas my true love sent to me\n12 drummers drumming\n11 pipers piping\n" \
               "10 lords a-leaping\nNine ladies dancing\nEight maids a-milking\nSeven swans a-swimming\n" \
               "Six geese a-laying\nFive golden rings\nFour calling birds\nThree french hens\nTwo turtle doves, and\n" \
               "A partridge in a pear tree\n"
    if verso == 1:
        print(verso_1, "\n")
    if verso == 2:
        print(verso_2, "\n")
    if verso == 3:
        print(verso_3, "\n")
    if verso == 4:
        print(verso_4, "\n")
    if verso == 5:
        print(verso_5, "\n")
    if verso == 6:
        print(verso_6, "\n")
    if verso == 7:
        print(verso_7, "\n")
    if verso == 8:
        print(verso_8, "\n")
    if verso == 9:
        print(verso_9, "\n")
    if verso == 10:
        print(verso_10, "\n")
    if verso == 11:
        print(verso_11, "\n")
    if verso == 12:
        print(verso_12, "\n")

verso = int(input("Inserisci Verso da Visualizzare: "))
dodici_giorni_natale(verso)
valore = 1
while valore != 12:
    dodici_giorni_natale(valore)
    valore = valore + 1
