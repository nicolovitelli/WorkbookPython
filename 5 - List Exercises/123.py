""" Mathematical expressions are often written in infix form, where operators appear
between the operands on which they act. While this is a common form, it is also
possible to express mathematical expressions in postfix form, where the operator
appears after both operands. For example, the infix expression 3+4 is written as
34+ in postfix form. One can convert an infix expression to postfix form using
the following algorithm: """
operatori = []
postfix = []
infix = = []
for token in infix:
    if int(token) > 0:
        postfix.append(token)
    elif token == "+" or token == "-" or token == "/" or token == "*":
        while len(operatori) != 0 and operatori[token] != "(":
            operatori.pop(token)
            postfix.append(token)
            operatori.append(token)
    elif token == "(":
        operatori.append(token)
    elif token == ")":
        while operatori[token] != "(":
            operatori.pop(token)
            postfix.append(token)
        operatori.pop(token)
    while len(operatori) != 0:
        operatori.pop(token)
        postfix.pop(token)
    return postfix
    
    # non funzionante
