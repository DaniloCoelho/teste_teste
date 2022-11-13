#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense

tabela = ('Corinthians' , 'Santos' , 'Palmeiras' , 'São Paulo' , 'Flamengo' , 'Fluminense' , 'Vasco' , 'Botafogo' , 'Inter' , 'Gremio' )

for i in range(0,5):
    print(f'O {i+1}° é {tabela[i]}')
print()
print(f'Os 5 primeiro são {tabela[0:5]}')
print()
for c in range(0,4):
    print(f'O {10-c}° é {tabela[9- c]}')
print()
print(f'Os 4 últimos são {tabela[-4:]}')
    
d = tabela.index('Vasco')
print()
print(f'Em ordem alfabetica{sorted(tabela)} e {tabela.index("Vasco")}')

print(f'O Vasco está na posição {d+1}°')