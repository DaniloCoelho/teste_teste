num1 = int(input('digite um número '))
num2 = int(input('digite outro número'))
print()
print(''' 1 para somar
             2 para multiplicar
             3 para comparar
             4 novos números
             5 sair''')
botao = int(input())
while not botao == 5:
    if botao == 1:
        soma = num1 + num2
        print('a soma é {} '.format(soma))
        botao = int(input('digite o desejado '))
    if botao == 2:
        mult = num1 * num2
        print('a multiplicação é {} '.format(mult))
        botao = int(input('digite o desejado '))
    if botao == 3:
        if num1 > num2 :
            print('{} é maior que {} '.format(num1,num2))
            botao = int(input('digite o desejado '))
        elif num1 < num2:
            print('{} é maior que {} '.format(num2 , num1))
            botao = int(input('digite o desejado '))
        elif num1 == num2:
            print('os numeros são iguais')
            botao = int(input('digite o desejado '))
        
     
    if botao == 4:
            print('digite novos números')
            print()
            num1 = int(input('digite um número '))
            num2 = int(input('digite outro número '))
            botao = int(input('digite o desejado '))
else:
 print('fim')
 
            
    