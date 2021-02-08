jogo1 = [1,2,4,5,6,7,9,10,11,13,15,16,17,21,25]

jogo2 = [3,4,8,10,11,12,14,17,18,19,20,22,23,24,25]
s1 = 0
s2 = 2
valor1 = 0
valor2 = 0
print('Lotofácil')
print()
entrada = input()
sorteado = []

if len(entrada)>15: #tratar string, tirar espaços
    list = entrada.split()
    entrada = ''.join(list)# juntar lista em unica str
    
else:
    pass

while len(sorteado)<15:
	sorteado.append(int(entrada[s1:s2]))
	s1 = s1 +2
	s2 = s2 +2
	
else:
	print()
	print(sorteado)
	print()

acertos1 =0
for I in jogo1:
      if I in sorteado:
         acertos1 =acertos1 +1
         
acertos2 =0
for I in jogo2:
      if I in sorteado:
         acertos2 =acertos2 +1
         
if acertos1 == 11:
     valor1 = 5
if acertos1 == 12:
     valor1 = 10
if acertos1 == 13:
     valor1 = 20
     
if acertos2 == 11:
     valor2 = 5
if acertos2 == 12:
     valor2 = 10
if acertos2 == 13:
     valor2 = 20
     
print("")    
print("jogo 1")                  
print(acertos1)
print()
print("jogo 2")
print(acertos2)
print()
print("valor a receber")
print(valor1 + valor2,",00")