queue = []
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')
print(queue)

while len(queue)>0:
	queue.pop(0)
	print(queue)

#fila c poucos itens