#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B)Em que posição foi digitado o primeiro valor3.
#C) Quais foram os números pares.

nums = (int(input()) , int(input()) , int(input()) , int(input()) , int(input()))
print(nums)
cont = 0
pares = []
for i in nums:
    if i % 2 == 0:
        pares.append(i)
    #if i == 9:
        #cont += 1

print(f' O 9 apareceu {nums.count(9)} vezes ')
if 3 in nums:
    print(f'O número 3 está na posição {nums.index(3)+1}')
else:
    print('nao tem o número 3')
print(f'Os números pares são {pares}')