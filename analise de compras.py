#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

soma = 0
caros = 0
nome = 0
nomebarato = 0
preco = 0
barato = 0
quer = 0

while True:
    nome = str(input(' produto  ')).strip()
    preco = int(input('valor  '))
    if soma == 0:
        nomebarato = nome
        barato = preco
    soma += preco
    
    
    if preco < barato:
        nomebarato = nome
        barato = preco
    if preco > 1000:
        caros += 1
    
    quer = str(input(' Deseja continuar? [S / N ]')).strip().upper()[0]
    
    while quer not in 'SN' :
         quer = str(input(' Deseja continuar? [S / N ]')).strip().upper()[0]
         
    if quer == 'N':
         break
         
print(f'''O valor gadto na compra é {soma}
{caros} produtos custaram mais de 1000 reias
o produto mais barato é {nomebarato}''')
         
     
     
     

    