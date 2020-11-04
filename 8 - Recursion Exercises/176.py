""" A spelling alphabet is a set of words, each of which stands for one of the 26 letters in the alphabet.
While many letters are easily misheard over a low quality or noisy communication channel, the words used to
represent the letters in a spelling alphabet are generally chosen so that each sounds distinct and is difficult
to confuse with any other. The NATO phonetic alphabet is a widely used spelling alphabet. Each letter and its
associated word is shown in Table 8.1. Write a program that reads of word from the user and then displays its phonetic
spelling. For example, if the user enters Hello then the program should output Hotel Echo Lima Lima Oscar. Your
program should use a recursive function to perform this task. Do not use a loop anywhere on your solution. Any 
non-letter characters entered by the user should be ignored. """
def otan(word):
  dictionary = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf', 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}
  phon = [dictionary[w] for w in word]
  return ' '.join(phon)

def main(): 
    word = input('Enter word: ')
    print(otan(word))

if __name__ == '__main__':
    main()
