import random
import time
filapre= []
filacom=[]
novasenhap= 0
novasenhac=0
senhachamada =0
ordem = 0
list = ['a' , 'p' , 'c']


while len(filapre)<1000:
	#botao = input()
	botao = random.choice(list)
	time.sleep(1.5)
	if botao=='a':
			if len(filapre)>0 or len(filacom)>0:
				if len(filapre)>0:
					if ordem <2:
						ordem = ordem+1
						print('preferencial',filapre[0])
						filapre.pop(0)
						botao = 0
					else:
						ordem =0
						print('comum',filacom[0])
						filacom.pop(0)
						botao = 0
				else:
					ordem = 0
					print('comum',filacom[0])
					filacom.pop(0)
					botao = 0
				
	elif botao=='p':
		novasenhap = novasenhap+1
		filapre.append(novasenhap)
		print('P',filapre)
		botao = 0
	elif botao=='c':
		novasenhac = novasenhac+1
		filacom.append(novasenhac)
		print('C',filacom)
		botao = 0
		
else:
	print('fila vazia')
	botao = 0