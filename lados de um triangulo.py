print('digite qual lado você quer  ')

lado = input("?")


if lado == 'hipotenusa' or lado == 'c':
	a1 = float(input("a= "))
	b1 = float(input('b= '))
	hip = float(( a1** 2 + b1 ** 2 )** 0.5)
	
	print("hipotenusa = " ,hip)
	
if lado == "cateto adjacente" or lado == "a":
	bx = float(input("b= "))
	cx = float(input("c= "))
	ca = float(cx** 2 - bx** 2  ** 0.5)
    print("Cateto adjacente "+ca )
else:
    print('nada')
    

    
	
