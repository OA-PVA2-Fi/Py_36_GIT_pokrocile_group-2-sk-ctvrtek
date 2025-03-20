from utils import secti, prepona_pravouhl_trojuhelniku


def main():
    x = 5
    y = 10
    vysledek = secti(x, y)
    print(f"Výsledek sčítání {x} a {y} je: {vysledek}")
    print(f"Délka přepony pravoúhlého trojúhelníku s odvěsnami {x} a {y} je: {prepona_pravouhl_trojuhelniku(x,y)}")

if __name__ == '__main__':
    main()