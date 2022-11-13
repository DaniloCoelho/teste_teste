#: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
maior = homem = femenor = 0
while True:
    idade = int(input('digite a idade  '))
    sexo = str(input('digite o sexo ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = input('digite o sexo ').strip().upper()[0]
    if idade >18:
        maior += 1
    if sexo in 'M':
        homem += 1
    if sexo in 'F' and idade < 20:
        femenor += 1
    sn = input('deseja continuar ?  ').strip().upper()[0]
    while sn not in 'SN':
        sn = input('deseja continuar ?  ').strip() .upper()[0]
    if sn in 'N':
        break
        
    
    
        
        
print(f'''O número de maiores de 18 é {maior}
O número de homens é {homem}
O número de mulheres menores de 20 é {femenor}''')
        