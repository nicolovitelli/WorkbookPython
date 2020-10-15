""" In this exercise you will create a program that reads a pressure from the user in kilopascals.
Once the pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres.
Use your research skills to determine the conversion factors between these units. """
pressione_kpa = float(input("Inserisci la pressione in kilopascal: "))
libbre_per_pollicequadrato = pressione_kpa / 6.89475729
millimetri_di_mercurio = pressione_kpa * 760 / 101.325
atmosfera = pressione_kpa / 101.325
print("Pressione convertita in Libbre per pollice quadrato:", round(libbre_per_pollicequadrato,2))
print("Pressione convertita in Millimetri di Mercurio:", round(millimetri_di_mercurio,2))
print("Pressione convertita in Atmosfera:", round(atmosfera,2))
