#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
pi = ['p','i']
c = 0
while True:
    esc = input('Escolha P para par e I para impar  ').strip().upper()[0]
    while esc not in 'PI':
        esc = input('Escolha P para par e I para impar  ').strip().upper()[0]
    num = int(input('escolha um número  '))
    numcom = random.randint(0,5)
    res = num + numcom
          
    if esc in 'Pp':
        if res % 2 == 0:
            print('Você ganhou!!! ')
            c += 1
        else:
            print('Você perdeu!!! ')
            break
    if esc in 'Ii':
        if res % 2 != 0:
            print('Você ganhou!!! ')
            c +=1
        else:
            print('Você perdeu!!!')
            break
print(f'Você ganhou {c} vezes seguidas')
    
    
    