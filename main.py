from utils import *

def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")
    vysledek2 = obvod_obdelniku(5,7)
    print(f"Obvod obdélníku je:", vysledek2)

if __name__ == '__main__':
    main()