#digite numeros e vao somando , se digitar 999 para e printa numero de vezes e soma deles

#c = 0
#s = 0
#u = int(input())
#while u != 999:
    #u = int(input()) 
    #c +=1
    #s += u
    #u = int(input())

 #s -= 99

#print('{} vezes , {} soma'.format(c , s))

#Depois 
c = s = 0
while True:
    n = int(input('Digite um número  '))
    if n == 999:
        break
    c +=1
    s += n
    
print(' Foram {} vezes e a soma é {}  '.format(c , s))
print(f' Foram {c} vezes e a soma é {s}  ')
