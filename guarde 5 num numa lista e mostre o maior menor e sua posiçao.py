#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
numeros = []
menor = 0
maior = 0
count = 0
for i in range(0,5):
    numeros.append(int(input(f'digite um numero na posição  {i}  ')))
    if i == 0:
        menor = numeros[i]
        maior = numeros[i]
    count += 1
    if numeros[i] < menor:
        menor = numeros[i]
    if numeros[i] > maior:
        maior = numeros[i]
    
a = numeros.index(menor)
b = numeros.index(maior)
    
print(f'O maior valor foi {maior} na posição {b} ')
for v , c in enumerate(numeros):
    if c == maior:
        print(f'Na posição {v}!!')
print(f'O menor valor foi {menor} na posição {a} ')
    