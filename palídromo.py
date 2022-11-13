frase = input('')
frase1 = frase.split()
frase2 = ''.join(frase1)
fraseinv = ''
for i in range(len(frase2)-1 , -1 ,-1):
    fraseinv += frase2[i]

if frase2 == fraseinv:
        print('isso é um palidromo')
    
else:
        print('isso não é um palídromo')
