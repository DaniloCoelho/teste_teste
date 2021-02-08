#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
nuns = []
for i in range(0,5):
    n = (int(input('Digite um número  ')))
    if i == 0 or n > nuns[-1]:
        nuns.append(n)
        print('adicionando no fim da lista')
    else:
        pos = 0
        while pos < len(nuns):
            if n <= nuns[pos]:
                nuns.insert(pos , n)
                print(f'Adicionado na posição {pos} ')
                break
            pos += 1
print('-'*30)
        
            
            
print(nuns)
        