from sys import argv

""" Unix-based operating systems typically include a tool named cat, which is short
for concatenate. Its purpose is to concatenate and display one or more files whose
names are provided as command line parameters. The files are displayed in the same
order that they appear on the command line.
Create a Python program that performs this task. It should generate an appropriate
error message for any file that cannot be displayed, and then proceed to the next file.
Display an appropriate error message if your program is started without any command
line parameters. """
if len(sys.argv) == 1:
    print("Devi inserire almeno un nome di un file.")
    quit()
for i in range(1, len(sys.argv)):
    fname = sys.argv[i]
    try:
        inf = open(fname, "r")
        for line in inf:
            print(line, end="")
        inf.close()
    except:
        print("Impossibile aprire", fname)
