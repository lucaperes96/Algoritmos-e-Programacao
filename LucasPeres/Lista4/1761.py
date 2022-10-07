# URL do Enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

n = 1 
soma = 0
while n!=0:
    n = float(input())
    soma = soma+n 
if n == 0:
    pag = float(input())
print("Total da compra: R$%.2f" %(soma))
print("Valor pago: R$%.2f" %(pag))
print("Troco: R$%.2f" %(pag-soma))