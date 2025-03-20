from utils import secti, obsah_ctverce


def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")

    vypocet_obsahu_ctv = obsah_ctverce(x)
    print(f'Obsah čtverce, když strana je dlouhá {x} se rovná {vypocet_obsahu_ctv}')


if __name__ == '__main__':
    main()



