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
        d2 = editDistance(s, t[0 : len(t) - 1]) + 1
        d3 = editDistance(s[0 : len(s) - 1], t[0: len(t) - 1]) + cost
        return min(d1, d2, d3)

def main():
    s1 = input("inserisci una stringa: ")
    s2 = input("inserisci un'altra stringa: ")
    print("distanza:", editDistance(s1, s2))

if __name__ == '__main__':
    main()
