from utils import *

def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")
    obvod_obdelniku_vysledek = obvod_obdelniku(5,7)
    print(f"Obvod obdélníku je:", obvod_obdelniku_vysledek)

if __name__ == '__main__':
    main()