filapre= []
filacom=[]
novasenhap= 0
novasenhac=0
senhachamada =0
ordem = 0


while len(filapre)<1000:
	botao = input()
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
		print(filapre)
		botao = 0
	elif botao=='c':
		novasenhac = novasenhac+1
		filacom.append(novasenhac)
		print(filacom)
		botao = 0
		
else:
	print('fila vazia')
	botao = 0