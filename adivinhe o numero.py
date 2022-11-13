import random
s = 0 
u = int(input('digite um numero de 1 a 10 '))
c = 1

while s != u:
    s = random.randint(1,10)
    u = int(input('digite um numero de 1 a 10 '))
    c += 1
    
print(c)
