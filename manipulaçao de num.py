#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = 0
list = []
escolha = 's'
medium= 0
num = 0
cont = 0
while escolha in 'Ss':
    num = int(input('insert num '))
    soma = soma + num
    cont += 1
    escolha = str(input('escolha S ou N '))
    if cont == 1:
        list.append(num)
    elif cont > 1 and num > list[0]:
        list.append(num)
    elif num < list[0]:
        list.insert(0, num)
        
    
    if not escolha in 'Ss' and escolha != 'n':
        print('error choice ')
        escolha = str(input(''))
    
    else:
        pass
    print('S or N')
        
medium = soma / cont

print('the medium of numbers is {} e foram {} vezes'.format(medium , cont))
print('maior {} e menor {}'.format(list[0] ,list[len(list)-1]))