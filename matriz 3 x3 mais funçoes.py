#087: Aprimore o desafio anterior, mostrando no final:                                      A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna.      C) O maior valor da segunda linha.
par = impar = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
col = 0
maior = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input('Digite um número  '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        else:
            impar += matriz[l][c]
        if c == 2:
            col += matriz[l][c]
        if l == 1:
            if maior == 0 or matriz[l][c] > maior:
                maior = matriz[l][c]
print('*'* 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:5^}]', end='')
    print()

print(f'a soma dos números pares são {par}')
print(f'a soma dos números impares são {impar}')
print(f'terceira coluna {col}')
print(f'o maior da segunda linha é {maior}')

#123
#456
#789