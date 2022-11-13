num = int(input('digite um numero '))
nprimo = 0

for i in range(1,num+1):
           if num % i == 0 and num != i and i != 1:
               nprimo = nprimo +1
               
if not nprimo >0:
        print('numero primo')
else:
        print('nao é primo')
        
        
          