""" Tokenizing is the process of converting a string into a list of substrings, known as
tokens. In many circumstances, a list of tokens is far easier to work with than the
original string because the original string may have irregular spacing. In some cases
substantial work is also required to determine where one token ends and the next one
begins.
In a mathematical expression, tokens are items such as operators, numbers and
parentheses. Some tokens, such as *, /, ˆ, ( and ) are easy to identify because the
token is a single character, and the character is never part of another token. The + and
- symbols are a little bit more challenging to handle because they might represent
the addition or subtraction operator, or they might be part of a number token """
def listaToken(s):
    s = s.replace(" ", "")
    tokens = []
    i = 0
    while i < len(s):
        if s[i] == "*" or s[i] == "/" or s[i] == "^" or\
            s[i] == "(" or s[i] == ")":
            tokens.append(s[i])
            i = i + 1
        elif s[i] == "+" or s[i] == "-":
            if i > 0 and (s[i - 1] >= "0" and s[i - 1] < s[i - 1] == ")"):
                tokens.append(s[i])
                i = i + 1
        elif s[i] >= "0" and s[i] <= "9":
            num = s[i]
            i = i + 1
            while i < len(s) and s[i] >= "0" and s[i] <= "9":
                num = num + s[i]
                i = i + 1
                tokens.append(num)
        else:
            return []
        return tokens
def main():
    exp = input("Inserisci un Espressione Matematica: ")
    tokens = listaToken(exp)
    print("I Token sono:", tokens)

main()
