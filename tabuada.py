#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
num = int(input('digite um número  '))


while num >= 0:
    for i in range(0 , 11):
        res = i * num
        print('{} x {} = {} '.format(num , i , res))
    num = int(input('digite um número  '))
else:
    print('Acabou!!!!')