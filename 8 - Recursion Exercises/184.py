""" Write a function that implements the recursive flattening algorithm described previously. Your function will take
one argument, which is the list to flatten, and it will return one result, which is the flattened list. Include a main
program that demonstrates that your function successfully flattens the list shown earlier in this problem, as well as
several others. """
def flatten(data):
    if data == []:
        return []
    if type(data[0]) == list:
        return flatten(data[0]) + flatten(data[1:])
    else:
        return [data[0]] + flatten(data[1:])

def main():
    print(flatten([1, [2, 3], [4, [5, [6, 7]]], [[[8,]], 9]]))
    print(flatten([1, [2, [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]]]))

if __name__ == '__main__':
    main()
