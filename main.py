from utils import secti
from utils import kraceni

def main():
    x = int(input("Kolik cm má strana a: "))
    y = int(input("Kolik cm má strana b: "))
    vysledek = kraceni(x,y)
    print(f"Výsledek obsahu obdelníku je:", vysledek,"cm2")

if __name__ == '__main__':
    main()