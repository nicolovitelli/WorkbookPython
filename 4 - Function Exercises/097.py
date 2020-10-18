""" Using your solutions to Exercises 94 and 96, write a program that generates a random
good password and displays it. Count and display the number of attempts that were
needed before a good password was generated. Structure your solution so that it
imports the functions you wrote previously and then calls them from a function
named main in the file that you create for this exercise. """
def buona_password():
    while controllo_password(password_random()) != True:
        password_random()
    print("Password Generata Casualmente:", password_random())

def main():
    buona_password()

if __name__ == '__main__':
    main()
