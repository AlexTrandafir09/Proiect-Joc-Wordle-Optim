import random
L=[]
for x in (open("cuvinte_wordle.txt","r")).read().strip().split():
    L.append(x)
cuv_corect=random.choice(open('cuvinte_wordle.txt').read().split())
# cuv_corect="ATOMI"
print(cuv_corect)
ok=0
nrcuvant=0
lista_culori=["X","X","X","X","X"]
while ok==0:
    ok_cazuri=1
    ok=1
    nrcuvant+=1
    cuv_citit=input(f"Incercarea numarul {nrcuvant} este: ")
    if cuv_citit.isupper()==False:
        print("Cuvintele sunt formate doar din litere mari")
        ok_cazuri=0
    if cuv_citit.isalpha()==False:
        print("Scrierea se face doar cu litere")
    if len(cuv_citit)!=5:
        print("Cuvintele trebuie sa aiba doar 5 litere")
        ok_cazuri=0
    if cuv_citit not in L:
        print("Cuvantul nu se afla in lista")
        ok_cazuri=0
    if ok_cazuri==1:
        for i in range (5):
            if cuv_citit[i]==cuv_corect[i]:
                lista_culori[i]="Verde"
            elif cuv_citit[i] in cuv_corect and cuv_citit[i] !=cuv_corect[i]:
                        lista_culori[i]="Galben"
            else:
                lista_culori[i]="Gri"

        for i in range(5):
            if lista_culori[i]!="Verde":
                ok=0
        if ok==1:
            print("Cuvant corect!")
            break
        else:
            print(*lista_culori)

    else:

        ok=0
        nrcuvant -= 1