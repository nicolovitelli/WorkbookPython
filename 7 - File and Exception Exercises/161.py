from sys import argv

""" When one writes a function, it is generally a good idea to include a comment that
outlines the function’s purpose, its parameters and its return value. However, sometimes comments are forgotten,
or left out by well-intentioned programmers that plan to write them later but then never get around to it.
Create a python program that reads one or more Python source files and identifies
functions that are not immediately preceded by a comment. For the purposes of this
exercise, assume that any line that begins with def, followed by a space, is the 
beginning of a function definition. Assume that the comment character, #, will be
the first character on the previous line when the function has a comment. Display the
names of all of the functions that are missing comments, along with the file name
and line number where the function definition is located.
The user will provide the names of one or more Python files as command line
parameters. If your program encounters a file that doesn’t exist or can’t be opened
then it should display an appropriate error message before moving on and processing the remaining files."""
if len(argv) == 1:
    print("Inserisci almeno un nome di un file")
    quit()
for fname in argv[1 : len(argv)]:
    try:
        inf = open(fname, "r")
        prev = " "
        lnum = 1
        for line in inf:
            if line.startswith("def ") and prev[0] != "#":
                bracket_pos = line.index("(")
                name = line[4 : bracket_pos]
                print("%s line %d: %s" % (fname, lnum, name))
                prev = line
                lnum = lnum + 1
        inf.close()
    except:
        print("problemi con il file", fname)
        print("spostamento di file")
