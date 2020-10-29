""" The edit distance between two strings is a measure of their similarity—the smaller the
edit distance, the more similar the strings are with regard to the minimum number of
insert, delete and substitute operations needed to transform one string into the other.
Consider the strings kitten and sitting. The first string can be transformed
into the second string with the following operations: Substitute the k with an s,
substitute the e with an i, and insert a g at the end of the string. This is the smallest
number of operations that can be performed to transform kitten into sitting.
As a result, the edit distance is 3. """
def editDistance(s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0
        if s[len(s) - 1] != t[len(t) - 1]:
            cost = 1
            d1 = editDistance(s[0 : len(s) - 1], t) + 1
            d2 = editDistance(s, t[0 : len(t - 1)]) + 1
            d3 = editDistance(s[0 : len(s) - 1], t[0 : len(t) - 1]) + cost
            return min(d1, d2, d3)
def main():
    s1 = input("inserisci stringa: ")
    s2 = input("inserisci altra stringa: ")
    print("distanza tra", s1, "e", s2, "è:", editDistance(s1, s2))

if __name__ == '__main__':
    main()
