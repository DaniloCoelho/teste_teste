#085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[],[]]
n = 0
for i in range(0,7):
    n = int(input('Digite um número  ')) 
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
        
sorted(lista[0])
sorted(lista[1])        
print('-'*30)
print(f'Os pares são {lista[0]}')
print(f'Os impares são {lista[1]} ')
    