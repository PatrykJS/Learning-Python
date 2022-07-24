import string
import random
proponowane = string.digits + string.ascii_letters


def tworzeniehasla():
    print("STWÓRZ HASŁO")
    print("Proponowane hasło: ")
    print("" .join(random.choice(proponowane) for podane in range(14)))

    haslo = input(str("\nPodaj nowe hasło: "))
    if len(haslo) < 8:
        print("Hasło jest za krótkie, minimalna ilość znaków (8)!")
        tworzeniehasla()
    elif haslo.isalpha():
        print("Hasło musi zawierać przynajmniej 1 cyfre!")
        tworzeniehasla()
    elif haslo.isnumeric():
        print("haslo musi zawierac przynajmniej 1 litere!")
        tworzeniehasla()
    else:
        print("prawidłowe hasło")

    powtorzhaslo = input("Powtórz hasło: ")
    haslo = haslo
    while powtorzhaslo == haslo:
        print("Próba tworzenia hasła powiodła się!")
        break
    else:
        print("Hasła sie nie zgadzają, tworzenie hasła nie powiodło się")
        tworzeniehasla()


if __name__ == "__passwrdcreator__":
    tworzeniehasla()
