#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
for p in range(1,5):
    print('------- {}° PESSOA ------'.format(p))
    nome = str(input('Nome ')).strip()
    idade = int(input('Idade '))
    sexo = str(input('Sexo '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
        
mediaidade = somaidade / 4
print('A média de idade do grupo é {} '.format(mediaidade))
print('A idade do homem mais velho é {} e o nome é {} '.format(maioridadehomem, nomevelho))
print('Tem {} mulheres com menos de 20 anos'.format(totmulher))