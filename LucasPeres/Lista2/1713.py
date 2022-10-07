# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

valorH = float(input())
horasT = int(input())

SalB = valorH*horasT
Impost = SalB*0.11
Inss = SalB*0.08
Sindc = SalB*0.05
Liquid = SalB-Impost-Inss-Sindc

print("Salário Bruto: R$%.2f" %(SalB))
print("Imposto: R$%.2f" %(Impost))
print("INSS: R$%.2f" %(Inss))
print("Sindicato: R$%.2f" %(Sindc))
print("Líquido: R$%.2f" %(Liquid))