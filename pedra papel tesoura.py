import random

lista = ['pedra' , 'papel' , 'tesoura']
com = random.choice(lista)
print('1 para pedra')
print('2 para tesoura')
print('3 para papel')
play = input('')
print('')
if play == '1':
    if com == 'pedra':
        print('Eu = Pedra x Pedra = Com')
        print('Empatou')
    elif com == 'tesoura':
        print('Eu = Pedra x Tesoura = Com')
        print('Você Ganhou !!!')
    elif com == 'papel':
        print('Eu = Pedra x Papel')
        print('Você perdeu!!!')
        
elif play == '2':
    if com == 'tesoura':
        print('Eu = Tesoura x Tesoura = Com')
        print('Empatou')
    elif com == 'pedra':
        print('Eu = Tesoura x Pedra = Com')
        print('Você Perdeu !!!')
    elif com == 'papel':
        print('Eu = Tesoura x Papel')
        print('Você Ganhou!!!')
        
elif play == '3':
    if com == 'papel':
        print('Eu = Papel x Papel = Com')
        print('Empatou')
    elif com == 'tesoura':
        print('Eu = Papel x Tesoura = Com')
        print('Você Perdeu !!!')
    elif com == 'pedra':
        print('Eu = Papel x Pedra = Com')
        print('Você Ganhou!!!')
        
