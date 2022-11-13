#81 Crie um programa que vai ler vários números e colocar em uma lista.  Depois disso mostre
#A) Quantos números foram digitados.            B) A lista de valores, ordenada de forma decrescente.                                   C) Se o valor 5 foi digitado e está ou não na lista.

num = []
esc = 'S'
c = 0
while True:
    n = int(input('Digite um número  '))
    num.append(n)
    c += 1
    esc = str(input('Deseja continuar S/N ? ')).strip().upper() 
    if esc in 'N':
        break
    while esc not in 'SN':
        print('Digite novamente S ou N')
        esc = str(input('Deseja continuar S/N ? ')).strip().upper()
        
print(f'Foram digitados {c} números')
num.sort(reverse = True)
print(num)
if 5 in num:
    print(f'Tem o número 5 na lista esta na posição {num.index(5)}')
    
    