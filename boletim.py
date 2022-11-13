#089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
# no   nome   media
# x     x       x
temp = []
princ = []
esc = 'S'

while True:
    nome = input('Digite o nome ')
    temp.append(nome)
    nota1 = float(input('Digite uma nota '))
    # verificar se é numerico---
    #while ....
    # nota1 = float(input('Digite uma nota '))
    
    
    temp.append(nota1)
    nota2 = float(input('Digite outra nota  '))
    temp.append(nota2)
    media = (nota1 + nota2)/2
    temp.append(media)
    princ.append(temp[:])
    temp.clear()
    print('-'*30)
    esc = input('Deseja adicionar mais nomes ?  S/N ').strip().upper()
    if esc in 'N':
        break
print()
print()
print()
print(f'{"No":<4}{"Nome":<10}{"Média":<10}')

for i in range(0,len(princ)):
    print(f'{i+1:<4}{princ[i][0]:<10}    {princ[i][3]:<10}')
    print('-'*30)