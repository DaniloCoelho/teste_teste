num = int(input('digite um número  '))
print('1》binário , 2》octal , 3》hexadecimal')
escolha = input('')

if escolha == '1':
        
        
        print('{} em binario é {} '.format(num , bin(num)[2:]))
  # entrega o binario com um codigo na frente entao tratamos essa string
        
elif escolha == '2':
    
    print('{} em octagonal é {} '.format(num , oct(num)[2:]))
    
elif escolha == '3':
    
    print('{} em hexadecimal é {} '.format(num , hex(num)[2:]))
    
