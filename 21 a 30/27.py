""" Write a program that computes the body mass index (BMI) of an individual. Your
program should begin by reading a height and weight from the user. Then it should 
use one of the following two formulas to compute the BMI before displaying it. If
you read the height in inches and the weight in pounds then body mass index is
computed using the following formula: BMI = weight / height × height × 703.
If you read the height in meters and the weight in kilograms then body mass index is computed using this slightly
simpler formula: BMI = weight / height × height ."""
print("1: Inserisci i Dati in pollici/libre\n2: Inserisci i Dati in metri/kg")
scelta = input("---> ")
if scelta == "1":
    altezza_pollici = float(input("Inserisci l'Altezza: "))
    peso_libre = float(input("Inserisci il Peso: "))
    imc_pl = peso_libre / (altezza_pollici * altezza_pollici) * 703
    print("Indice di Massa Corporea: ", round(imc_pl,2))
elif scelta == "2":
    altezza_metri = float(input("Inserisci l'Altezza: "))
    peso_kg = float(input("Inserisci il Peso: "))
    imc_mk = peso_kg / altezza_metri * altezza_metri
    print("Indice di Massa Corporea: ", round(imc_mk, 2))
elif scelta != "1" or scelta != "2":
    print("Scelta non valida")
