penny_per_nichel = 5
nichel = 0.05
totale = 0.0
prezzo = input("Inserisci il Prezzo (vuoto per uscire): ")
while prezzo != "":
    totale = totale + float(prezzo)
    prezzo = input("Inserisci il Prezzo (vuoto per uscire): ")
print("Totale da pagare:", totale)
arrotondamento = totale * 100 % penny_per_nichel
if arrotondamento < penny_per_nichel / 2:
    totale_contanti = totale - arrotondamento / 100
else:
    totale_contanti = totale + nichel - arrotondamento / 100
print("Totale da pagare in contanti:", totale_contanti)
