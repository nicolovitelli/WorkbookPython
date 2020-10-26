""" Write a program that displays the word (or words) that occur most frequently in a
file. Your program should begin by reading the name of the file from the user. Then
it should find the word(s) by splitting each line in the file at each space. Finally,
any leading or trailing punctuation marks should be removed from each word. In
addition, your program should ignore capitalization. As a result, apple, apple!,
Apple and ApPlE should all be treated as the same word. You will probably find
your solution to Exercise 111 helpful when completing this problem. """
def common_words(nomefile):
    wordDict = {}
    for line in nomefile:
        wordList = nomefile.split()
        for word in wordList:
            if word in wordDict:
                wordDict[word] = wordDict[word] + 1
            else:
                wordDict = 1
    return wordDict

def main():
    nomefile = input("Inserisci Nome del FIle: ")
    common_words(nomefile)

if __name__ == '__main__':
    main()
