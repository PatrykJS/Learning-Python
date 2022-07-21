import string
import random
proponowane = string.digits + string.ascii_letters

def tworzeniehasla():
    print("STWÓRZ HASŁO")
    print("Proponowane hasło: ")
    print("" .join(random.choice(proponowane) for i in range(14)))

    haslo = input(str("\nPodaj nowe hasło: "))
    if len(haslo) < 8:
        print("Hasło jest za krótkie, minimalna ilość znaków (8)!")
    elif haslo.isalpha():
        print("Hasło musi zawierać przynajmniej 1 cyfre!")
    elif haslo.isnumeric():
        print("haslo musi zawierac przynajmniej 1 litere!")
    else:
        print("prawidłowe hasło")
    powtorzhaslo = input("Powtórz hasło: ")
    if powtorzhaslo == haslo:
        print("Hasła się zgadzają!")
    else:
        print("Hasła nie zgadzają się!")

tworzeniehasla()