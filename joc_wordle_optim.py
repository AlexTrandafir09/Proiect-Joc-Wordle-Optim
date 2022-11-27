import math
from itertools import product
import random


def permutari():
    matrice_culori = []
    c = ["Gri", "Galben", "Verde"]
    for x in product(c, repeat=5):
        matrice_culori.append(x)
    return matrice_culori


def entropie_cuv(l):
    return l[1]


def functie_cuv_cu_cea_mai_mare_entropie():
    matrice_cuvinte = []
    matrice_culori = permutari()
    for x in L:
        entropie_medie = 0
        nr_cuv_potrivite = [0] * (3 ** 5)
        for z in L:
            rezultat = ()
            for i in range(5):
                if x[i] == z[i]:
                    rezultat += ('Verde',)
                else:
                    if z.find(x[i]) != -1:
                        rezultat += ('Galben',)
                    else:
                        rezultat += ('Gri',)
            nr_cuv_potrivite[matrice_culori.index(rezultat)] += 1
        for i in range(3 ** 5):
            caz = nr_cuv_potrivite[i] / len(L)
            if caz != 0:
                entropie_medie += caz * math.log2(1 / caz)
        linie_matrice = []
        linie_matrice.append(x)
        linie_matrice.append(entropie_medie)
        matrice_cuvinte.append(linie_matrice)
        matrice_cuvinte.sort(key=entropie_cuv, reverse=True)
    return (matrice_cuvinte[0][0])


def functie_verificare(cuv_corect, cuv_optim):
    global L
    rezultat = [0] * 5
    for i in range(5):
        if cuv_optim[i] == cuv_corect[i]:
            rezultat[i] = "Verde"
            L = [x for x in L if cuv_optim[i] == x[i]]
        elif cuv_optim[i] in cuv_corect:
            rezultat[i] = "Galben"
            L = [x for x in L if cuv_optim[i] in x and cuv_optim[i] != x[i]]
        else:
            rezultat[i] = "Gri"
            L = [x for x in L if cuv_optim[i] not in x]


L = []
matrice_incercari = []


def main():
    global L
    L = open("Cuvinte_wordle.txt", "r").read().strip().split()
    corect = random.choice((open("cuvinte_wordle.txt", "r")).read().strip().split())
    print(f"Cuvantul care trebuie ghicit este: {corect}")
    nr_incercari = 0
    cuv_optim = "TAREI"
    with open("tranzitie.txt", "r+") as f:
        f.write(cuv_optim)
    while cuv_optim != corect:
        nr_incercari += 1
        with open("tranzitie.txt", "r+") as f:
            cuv_optim = f.read()
        functie_verificare(corect, cuv_optim)
        with open("tranzitie.txt", "r+") as f:
            f.write(functie_cuv_cu_cea_mai_mare_entropie())
        print(f"Incercarea numarul {nr_incercari} este: {cuv_optim}")
    print("Raspuns corect")


main()