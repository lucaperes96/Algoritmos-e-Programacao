# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

Plano = input()
sal = float(input())

if Plano=="A":
    print("Novo salário: R$%.2f" %(sal*1.10))
    
elif Plano=="B":
    print("Novo salário: R$%.2f" %(sal*1.15))

elif Plano=="C":
    print("Novo salário: R$%.2f" %(sal*1.20))
    
else:
    print("OPÇÃO INVÁLIDA!")