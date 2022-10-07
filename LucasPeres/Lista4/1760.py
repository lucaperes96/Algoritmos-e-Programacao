# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

cont = 0
mediai = 0 
pessoas = 0
while cont<4:
    idade = float(input())
    mediai = mediai+idade
    peso = float(input())
    cont = cont+1
    if peso>90:
        pessoas = pessoas+1 
idadem = mediai/4
print("Qtd pessoas > 90 Kg: %i \n" "Idade média: %.2f" %(pessoas,idadem))