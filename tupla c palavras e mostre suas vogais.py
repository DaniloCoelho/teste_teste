#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

name = (str(input('digite uma palavra ')),str(input('digite uma palavra ')),str(input('digite uma palavra ')),str(input('digite uma palavra ')))  
count = 0
for c in name:
    print(f'Na palavra {c}')
    
    for i in c:
        if i in 'aeiou':
            
            if count == 0:
                print(f' tem as seguinte vogais' )
                print(f';" {i} "')
            else:
                print(f'" {i} "')
            count +=1
         
    if count < 1:
        print('Essa palavra não tem vogal')
    count = 0
