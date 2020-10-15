""" An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order. """
peso_widget = 75 # grammi
peso_gizmo = 112 # grammi
widget = int(input("Inserisci il numero di Widget: "))
gizmo = int(input("Inserisci il numero di Gizmo: "))
tot_widget = widget * peso_widget
tot_gizmo = gizmo * peso_gizmo
print("Peso totale ordine:", tot_gizmo + tot_widget, "grammi")
