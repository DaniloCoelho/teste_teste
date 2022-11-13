from typing import List

stack: List[str] = []

stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')

while len(stack)>0:
	top_item = stack.pop()## retorna ultimo item
	print(top_item)

#for item in stack[::-1]:# retorna listade tras p frente
	#print(item)





#print(stack, top_item)
