# URL do Enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

anoatual = int(input())
anoinic = 2006
aument = 1.015
salinc = 1000
saltotal = aument*salinc
if anoatual>=anoinic:
    while anoinic<anoatual:
        saltotal = saltotal*(aument+0.01)
        anoinic = anoinic+1 
        aument = aument+0.01
    print("Salário atual: R$%.2f" %(saltotal))
else:
    print("O ano informado deverá ser > 2005!")