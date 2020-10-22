""" In a Canadian postal code, the first, third and fifth characters are letters while the
second, fourth and sixth characters are numbers. The province can be determined
from the first character of a postal code, as shown in the following table. No valid
postal codes currently begin with D, F, I, O, Q, U, W, or Z. """
provincie = dict()
provincie['Newfoundland'] = 'A'
provincie['Nova Scotia'] = "B"
provincie['Prince Edward Islan'] = "C"
provincie['New Brunswick'] = "E"
provincie['Quebec'] = "G" or "H" or "J"
provincie['Ontario'] = "K" or "L" or "M" or "N" or "P"
provincie['Manitoba'] = "R"
provincie['Saskatchewan'] = "S"
provincie['Alberta'] = "T"
provincie['British Columbia'] = "V"
provincie['Nunavut'] = "X"
provincie['Northwest Territories'] = "X"
provincie['Yukon'] = "Y"

provincia = input("Inserisci Provincia: ")
for c in sorted(provincie):
    if provincia == provincie[c]:
        print("Provincia", provincie[c], "trovata")
        for k in provincie:
            if provincie[k] == provincie[c]:
                print(provincie[k])
        raise LookupError
