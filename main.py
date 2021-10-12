'''
Returneaza true daca n este prim si false daca nu.
'''
from math import *
def is_prime(n):
    '''
    is_prime determina daca un numar este prim sau nu
    :param n: este numar intreg
    :return: True daca este prim si False daca nu este prim
    '''
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
    p=1
    for i in lst:
        p=p*i
    return p
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
    r = x % y
    while r!=0:
        x=y
        y=r
        r=x%y
    return y
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
    while x!=y:
        if x>y:
            x=x-y
        else: y=y-x
    return x

optiune = '''
Introduceti optiunea dumneavoastra: - 'prim' pentru a verifica primalitatea unui numar
                                    - 'produs' pentru a calcula produsul unei liste cu n elemente
                                    - 'comun' pentru a calcula cmmdc-ul a 2 numere
                                    - 'stop' pentru a opri programul
'''
def main():
    alegere = input(optiune)
    while alegere.lower()!= 'stop':
        if alegere.lower() == 'prim':
            numar = input("Introduceti numarul dumneavoastra: ")
            if is_prime(int(numar))==True:
                print("Numarul este prim")
            else: print("Numarul nu este prim")
        elif alegere.lower() == 'produs':
            lista = []
            print("Introduceti fiecare numar din lista, urmat de tasta ENTER: , pentru a oprit introducerea numerelor, scrieti 'stop' ")
            while True:
                m=input()
                if m.lower()=='stop':
                    break
                else: lista.append(int(m))
            if not lista:
                print("Produsul elementelor listei este: 0")
            else :print(f"Produsul elementelor listei este: {get_product(lista)}")
        elif alegere.lower()== 'comun':
            alegere_metoda = input("Pentru metoda scaderilor repetate, scrie '1', pentru metoda impartirilor repetate, scrie '2'")
            if alegere_metoda== '1':
                optiune1 = input("Introduceti primul numar ")
                optiune2 = input("Introduceti al doilea numar ")
                print(f"Cel mai mare divizor comun al celor doua numere este {get_cmmdc_v1(int(optiune1), int(optiune2))}, calculat prin metoda scaderilor repetate")
            else:
                optiune1 = input("Introduceti primul numar ")
                optiune2 = input("Introduceti al doilea numar ")
                print(f"Cel mai mare divizor comun al celor doua numere este {get_cmmdc_v1(int(optiune1), int(optiune2))}, calculat prin metoda impartirilor repetate")
        if alegere.lower() == 'stop':
            break
        else: alegere = input(optiune)
if __name__ == '__main__':
    main()
