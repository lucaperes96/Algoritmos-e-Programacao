# URL do Enunciado
# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1019

segu = int(input())
hor = segu/3600
mini = (segu%3600)/60
seg = (segu%3600)%60
print("%i:%i:%i" %(hor,mini,seg))