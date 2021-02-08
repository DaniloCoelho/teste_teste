from datetime import date
lista = []
menor = 0
maior = 0
for i in range(0,7):
    nasc = int(input())
    lista.append(date.today().year - nasc)
    
for i in lista:
    if i >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
        
        
        
print(''' são {} maiores de idade

e {} menores de idade'''.format(maior , menor))
    