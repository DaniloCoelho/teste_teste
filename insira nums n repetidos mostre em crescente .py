#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

nuns = []
while True:
    num = int(input('digite um numero '))
    if num in nuns:
        print('Esse número já está na lista ')
    else:
        nuns.append(num)
    escolha = str(input('Deseja continuar [S/N]  ')).strip().upper ()
    if escolha in 'N':
        break
    while escolha not in 'SN':
        print('Opção inválida')
        escolha = str(input('Deseja continuar [S/N]  ')).strip().upper()
        
        
print(f'Os números são {sorted(nuns)}')