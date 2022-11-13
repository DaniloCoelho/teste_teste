#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random

list = []
for i in range(0,5):
    i = random.randint(0,10)
    print(f'número gerado {i}')
    list.append(str(i))
v = ''.join(list)
print(f'em tupla({v})')

c = 0
menor = 0
maior = 0
for m in v:
    c += 1
    if c == 1:
        maior = m
        menor = m
    else:
        if m < menor:
            menor = m
        elif m > maior:
            maior = m
            
print(f'maior {maior} , menor {menor}')

# resoluçao no curso---------------------------------
print('----' *20)

n = (random.randint(0,10) , random.randint(0,10) ,random.randint(0,10), random.randint(0,10) ,random.randint(0,10) )
   
print(f'em tupla{n}')
print(f'maior {max(n)} , menor {min(n)}')
        
    
    