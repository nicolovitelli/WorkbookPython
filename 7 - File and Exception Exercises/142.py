from sys import argv

""" Unix-based operating systems also typically include a tool named tail. It displays
the last 10 lines of a file whose name is provided as a command line parameter.
Write a Python program that provides the same behavior. Display an appropriate
error message if the file requested by the user does not exist or if the command line
parameter is omitted.
There are several different approaches that can be taken to solve this problem.
One option is to load the entire contents of the file into a list and then display the
last 10 elements. Another option is to read the contents of the file twice, once to
count the lines, and a second time to display the last 10 lines. However, both of these
solutions are undesirable when working with large files. Another solution exists that
only requires you to read the file once, and only requires you to store 10 lines from
the file at one time. For an added challenge, develop such a solution. """
numero_righe = 10
lines = []
if len(sys.argv) != 2:
    quit()
try:
    inf = open(sys.argv[1], "r")
    for line in inf:
        lines.append(line)
        if len(lines) > numero_righe:
            lines.pop(0)
    inf.close()
except:
    print("Errore mentre si processa il file.")
    quit()
for line in lines:
    print(line, end="")
