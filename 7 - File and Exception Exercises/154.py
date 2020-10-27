""" The baby names data set consists of over 200 files. Each file contains a list of 100
names, along with the number of times each name was used. There are two files for
each year: one containing names used for girls and the other containing names used
for boys. The data set includes data for every year from 1900 to 2012.
Write a program that reads every file in the data set and identifies all of the names
that were most popular in at least one year. Your program should output two lists:
one containing the most popular names for boys and the other containing the most
popular names for girls. Neither of your lists should include any repeated values. """
first_year = 1900
last_year = 2012
def LoadAndAdd(fname, names):
    inf = open(fname, "r")
    line = inf.readline()
    inf.close()
    parts = line.split()
    name = parts[0]
    if name not in names:
        names.append(name)
def main():
    girls = []
    boys = []
    for year in range(first_year, last_year + 1):
        girl_fname = "../Data/BabyNames/" + str(year) + "_GirlsNames.txt"
        boy_fname = "../Data/BabyName/" + str(year) + "_BoysNames.txt"
        LoadAndAdd(girl_fname, girls)
        LoadAndAdd(boy_fname, boys)
    print("Girls names that reached 1:")
    for name in girls:
        print(" ", name)
    print()
    print("Boys names that reached 1:")
    for name in boys:
        print(" ", name)

main()
