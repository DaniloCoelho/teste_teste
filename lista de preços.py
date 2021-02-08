#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

table = ('a', 2.25 , 'b' ,3.20 , 'cd' , 4 , 'ecf' , 5.75)

print('Lista de preços')
print('-' *20)
for i in range(0 , len(table)):
    if i % 2 == 0:
        print(f'{table[i]:.<20}' , end =' ')# esquerda
    else:
        print(f'R${table[i]:>5.2f}')# direita
        