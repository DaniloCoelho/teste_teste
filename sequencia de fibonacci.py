n1 = int(input())
n2 = int(input())
n3 = 0
c = 0
v = int(input(' quantas vezes  '))
print('$$$'*10)

while c <= v:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    c +=1