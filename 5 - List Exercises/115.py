""" Pig Latin is a language constructed by transforming English words. While the origins of the language are unknown,
it is mentioned in at least two documents from the nineteenth century, suggesting that it has existed for more than
100 years. The following rules are used to translate English into Pig Latin:
• If the word begins with a consonant (including y), then all letters at the beginning of
the word, up to the first vowel (excluding y), are removed and then added to the end
of the word, followed by ay. For example, computer becomes omputercay
and think becomes inkthay.
• If the word begins with a vowel (not including y), then way is added to the end
of the word. For example, algorithm becomes algorithmway and office
becomes officeway.
Write a program that reads a line of text from the user. Then your program should
translate the line into Pig Latin and display the result. You may assume that the string
entered by the user only contains lowercase letters and spaces. """
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
