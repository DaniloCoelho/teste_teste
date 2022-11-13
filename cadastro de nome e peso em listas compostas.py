#  084: Faça um programa que leia nome e peso de várias pessoas,                     guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas.        B) Uma listagem com as pessoas mais pesadas.   C) Uma listagem com as pessoas mais leves.
esc = 'S'
nome = ''
peso = ''
lista1 = []
lista2 = []
c = 0
pesado = 0
leve = 0

while True:
    nome = input('Digite um nome  ')
    lista1.append(nome)
    peso = int(input('Digite o peso  '))
    if c == 0:
        pesado = peso
        leve = peso
    elif peso > pesado:
        pesado = peso
    elif peso < leve:
        leve = peso
        
    c += 1
    lista1.append(peso)
    lista2.append(lista1[:])
    lista1.clear()
    esc = input('Deseja adicionar mais pessoas ?  S/N ').strip().upper()
    
    if esc in 'N':
        break
print('-'*30)
print(f'O maior peso é {pesado} de :')
for i in lista2:
    if pesado in i :
        print(f' {i[0]}')
print(f'O menor peso é {leve} de :')
for i in lista2:
    if leve in i:
        print(f' {i[0]}')

print(f'Cadastrados {lista2}')
print(f'foram {c} cadastrados')
    
    
    
    
    