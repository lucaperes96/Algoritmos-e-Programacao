# URL do Enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

comprador = int(input())
valorP = float(input())

if comprador==1:
    print("Valor total a ser pago: R$%.2f" %(valorP))
    
elif comprador==2:
    print("Valor total a ser pago: R$%.2f" %(valorP - (valorP*0.13)))

elif comprador==3:
    print("Valor total a ser pago: R$%.2f" %(valorP - (valorP*0.07)))
    
else:
    print("OPÇÃO INVÁLIDA!")