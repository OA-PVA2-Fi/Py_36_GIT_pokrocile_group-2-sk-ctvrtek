from utils import secti,obvod_ctverce

def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")

    vypocet_obvodu_ctv = obvod_ctverce(x)
    print(f"Obvod čtverce je: {vypocet_obvodu_ctv}")


if __name__ == '__main__':
    main()


