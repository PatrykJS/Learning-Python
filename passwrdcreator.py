import string
import random
GenericPassword = string.digits + string.ascii_letters


def makepasswrd():
    print("PASSWORD CREATOR")
    print("Suggested Password: ")
    print("" .join(random.choice(GenericPassword) for p in range(14)))

    passwrd = input(str("\nDefine new password: "))
    if len(passwrd) < 8:
        print("Password is to short, minimal lenght (8)!")
        makepasswrd()
    elif haslo.isalpha():
        print("Password requires at least one digit!")
        makepasswrd()
    elif haslo.isnumeric():
        print("Password requires at least one letter!")
        makepasswrd()
    else:
        print("Correct password")

    repeatpasswrd = input("Repeat password: ")
    passwrd = passwrd
    while repeatpasswrd == passwrd:
        print("Password creation complete!")
        break
    else:
        print("Given passwords differ to each other, password creation failed.")
        makepasswrd()


if __name__ == "__passwrdcreator__":
    makepasswrd()
