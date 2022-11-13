#faça uma progressao que te de a opçao de pedir mais termos 

n = int(input())
r = int(input())
c = 1
print()
print(n)
mais = 0
p = 10
while c <= p:
    n = n + r
    c += 1
    print(n)
    if c == p:
        mais = int(input('quantos termos mais?  '))
        if mais > 0:
            p += mais
        else:
            pass
            