from utils import secti, slichobezniku

def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")

def lichobeznik():
    a = 10
    c = 5
    v = 3
    vysledek = slichobezniku(a,c,v)
    print('Obsah lichoběžníku vyšel ' + str(vysledek))


if __name__ == '__main__':
    main()
    lichobeznik()
