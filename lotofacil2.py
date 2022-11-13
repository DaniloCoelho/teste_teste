jogo1 = [1,2,4,5,6,7,9,10,11,13,15,16,17,21,25]

jogo2 = [3,4,8,10,11,12,14,17,18,19,20,22,23,24,25]

valor1 = 0
valor2 = 0

sorteado = []
sorteado = eval('[' + input() + ',' + input()+ ',' + input() + ',' + input() + ',' + input() + ',' + input() + ',' + input() + ',' + input() + ',' + input() + ',' + input() + ',' + input() + ',' + input() + ',' + input() + ',' +input() + ',' + input() + ']')

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
if acertos1 == 12:
     valor2 = 10
if acertos1 == 13:
     valor2 = 20
     

print()
print("jogo 1")                  
print(acertos1)
print()
print("jogo 2")
print(acertos2)
print()
print("valor a receber")
print(valor1 + valor2)
