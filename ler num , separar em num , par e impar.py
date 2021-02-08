#082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
num = []
par = []
impar = []
esc = 'S'

while True:
    n = int(input(('Digite um número = ')))
    num.append(n)
    
    if n % 2 == 0:
        par.append(n)
        
    else:
        impar.append(n)
        
    esc = str(input('Deseja continuar ? ( S / N - ')).strip().upper()
    while esc not in 'SN':
        print('Opção Inválida ')
        esc = str(input('Deseja continuar ? ( S / N - ')).strip().upper()
    if esc in 'N':
        break
    else:
        pass
        
print(f'Todos os números são {num}')        
print(f'Os números pares são {par}')
print(f'Os números ímpares são {impar}')

