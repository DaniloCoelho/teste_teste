print('calculadora de área de circulo' ) 
print('circuferência , área lateral , área total ')
d = float(input("diametro = "))
print()
print("digite a = para área")
print()
print("digite c = para circuferência")
print()
print("digite al = para área lateral")
print()
print("digite at = para área total")
print()

escolhido = input("")
print()

if escolhido == "a":
	aa = float(3.1416*((d/2)**2))
	print()
	print("área = ",aa)
	
if escolhido == "c":
	cc= float(2*3.1416*(d/2))
	print()
	print("circufêrencia =",cc)

if escolhido == "al":
	h = float(input("digite a altura = "))
	aal= float(2*3.1416*(d/2)*h)
	print()
	print("área lateral = ",aal)
	
if escolhido == "at":
	h = float(input("digite a altura = "))
	aa = float(3.1416*((d/2)**2))
	aal= float(2*3.1416*(d/2)*h)
	att= float(2*aa + aal)
	print()
	print("área total = ",att)
	
