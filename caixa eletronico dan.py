#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
resta = cont50 = cont20 = cont10 = cont1 = 0

while True:
    resta = int(input(' Qual valor sacar?  '))
    #resta = saque
    while resta >= 50:
        cont50 += 1
        resta -= 50
    while resta < 50 and resta >= 20:
        cont20 += 1
        resta -= 20
    while resta < 20 and resta >= 10:
        cont10 += 1
        resta -= 10
    while resta < 10 and resta >= 1:
        cont1 += 1
        resta -= 1
    if resta <= 0:
        print(f'''foram {cont50} notas de 50 
foram {cont20} notas de 20 
foram {cont10} notas de 10
foram {cont1} notas de 1 ''')
        
        break