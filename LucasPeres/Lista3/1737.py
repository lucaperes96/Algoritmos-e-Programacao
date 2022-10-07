# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

n = int(input())
aux = n
soma = 0
if n> 0:
    while aux>0:
        x = float(input())
        soma = soma+x
        aux = aux-1
    print("Soma dos números informados: %.2f" %(soma))
else:
    print("Informe uma quantidade > 0!")