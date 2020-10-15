""" Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places. """
interessi_per_anno = 4 # %
deposito = float(input("Inserisci la quantità di soldi depositati nell'account: "))
primo_anno = (deposito * interessi_per_anno) / 100
secondo_anno = (deposito * (interessi_per_anno * 2)) / 100
terzo_anno = (deposito * (interessi_per_anno * 3)) / 100
print("Totale Interessi dopo il primo anno: %.2f$" % primo_anno)
totale_anno1 = deposito + primo_anno
print("-> per un totale di: %.2f$" % totale_anno1)
print("Totale Interessi dopo il secondo anno: %.2f$" % secondo_anno)
totale_anno2 = deposito + secondo_anno
print("-> per un totale di: %.2f$" % totale_anno2)
print("Totale Interessi dopo il terzo anno: %.2f$" % terzo_anno)
totale_anno3 = deposito + terzo_anno
print("-> per un totale di: %.2f$" % totale_anno3)
