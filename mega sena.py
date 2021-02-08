#088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
from time import sleep

lista = []
jogos = int(input('Quantos jogos você quer ? '))

for j in range(1,jogos+1):
    for i in range(1,7):
        n = random.randint(1,60)
        while n in lista:
            n = random.randint(1,60)
        else:
            lista.append(n)
    lista.sort()
    print(f'jogo {j} = ',lista)
    lista.clear()
    sleep(2)
            
        