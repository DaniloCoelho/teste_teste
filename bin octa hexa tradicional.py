num = int(input('digite um número  '))
print('1》binário , 2》octal , 3》hexadecimal')
bin = []
escolha = input('')

if escolha == 'a':
    while num > 0:
        bin.insert(0 , int((num % 2)))
        num = num // 2
    else:
        bin2 = ''.join(bin)
        print('em binário é ', bin2)
        
elif escolha == 2:
    
    print('em binario é {} '.format())
elif escolha == 3:
    
    print('em binario é {} '.format())
    
