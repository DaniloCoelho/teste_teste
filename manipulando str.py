frase = input()
lista = frase.split() #separar string em lista
lista2 = []
for i in lista: 
    lista2.append(int(i))
      # transformando string em inteiro
      
      
frase2 = '^-'.join(lista)
frase3 = ''.join(lista) # juntando a lista em uma str
print('frase' ,frase)
print('lista' ,lista)
print('lista2' ,lista2)
print('frase2' ,frase2)
print('frase3' ,frase3)