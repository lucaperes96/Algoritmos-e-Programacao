# URL do Enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = input()
horex = float(input())

salmin = 1192.40
valhorex = 10

salex = horex * valhorex

salbrt = 3*salmin + salex

if salbrt > 2000:
    inss = salbrt*0.12
    if salbrt > 2500:
        impost = salbrt*0.20
    else:
        impost = salbrt
else:
    inss = salbrt*0.05

saliquid = salbrt - (inss+impost)

print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f" %(salbrt))
print("Salário líquido: R$%.2f" %(saliquid))