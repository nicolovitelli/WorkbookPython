""" This exercise examines the process of identifying the maximum value in a collection
of integers. Each of the integers will be randomly selected from the numbers between
1 and 100. The collection of integers may contain duplicate values, and some of the
integers between 1 and 100 may not be present.
Take a moment and think about how you would handle this problem on paper.
Many people would check each integer in sequence and ask themself if the number
that they are currently considering is larger than the largest number that they have seen
previously. If it is, then they forget the previous maximum number and remember
the current number as the new maximum number. This is a reasonable approach,
and will result in the correct answer when the process is performed carefully. If you
were performing this task, how many times would you expect to need to update
the maximum value and remember a new number? """
numero_max = randrange(1, 100)
aggiornato = 0
for i in range(100):
    casuale = randrange(1,99)
    print("numero uscito:", casuale)
    if casuale > numero_max:
        numero_max = casuale
        aggiornato = aggiornato + 1
        print("numero massimo aggiornato")
print("il valore massimo incontrato è stato:", numero_max)
print("il valore è stato aggiornato", aggiornato, "volte")

