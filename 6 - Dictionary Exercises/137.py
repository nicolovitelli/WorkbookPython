""" In the game of Scrabble™, each letter has points associated with it. The total score
of a word is the sum of the scores of its letters. More common letters are worth fewer
points while less common letters are worth more points. The points associated with
each letter are shown below: 
Write a program that computes and displays the Scrabble™ score for a word.
Create a dictionary that maps from letters to point values. Then use the dictionary to
compute the score."""
SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

def scrabble_score(word):
    total = 0
    for letter in word:
        total += SCORES[letter]
    return print("Il totale è:", total)

def main():
    word = input("Inserisci Parola: ")
    scrabble_score(word)

if __name__ == '__main__':
    main()
