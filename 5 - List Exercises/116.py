""" Extend your solution to Exercise 115 so that it correctly handles uppercase letters and
punctuation marks such as commas, periods, question marks and exclamation marks.
If an English word begins with an uppercase letter then its Pig Latin representation
should also begin with an uppercase letter and the uppercase letter moved to the end of
the word should be changed to lowercase. For example, Computer should become
Omputercay. If a word ends in a punctuation mark then the punctuation mark
should remain at the end of the word after the transformation has been performed.
For example, Science! should become Iencescay!. """
ay = "ay"
way = "way"
consonante = ("B","C", "D","F","G","H","J","K","L","M","N","P","Q","R","S","T","Y","V","X","Z")
vowel = ("A","E","I","O","U")
parola_utente = input("Inserisci una parola da tradurre: ")
prima_lettera = parola_utente[0]
prima_lettera = str(prima_lettera)
prima_lettera=prima_lettera.upper()
if prima_lettera in consonante:
    print(prima_lettera,"è una consonante")
    lunghezza_parola = len(parola_utente)
    rimuovi_prima_lettera = parola_utente[1:lunghezza_parola]
    pig_latin=rimuovi_prima_lettera+prima_lettera+ay
    print("La parola in Pig Latin è:",pig_latin)
elif prima_lettera in vowel:
    print(prima_lettera,"is a vowel")
    pig_latin=parola_utente+way
    print("La parola in Pig Latin è:",pig_latin)
else:
    print("Non so cosa",prima_lettera,"sia")
