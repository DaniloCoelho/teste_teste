# crie um programa que leie o nome de uma pessoa e diga se ela tem " Silva" no nome
nome = str(input('qual é seu nome completo? ')).strip()
# comando strip tira os espaços desnecessarios
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
# existe silva no nome? 
# nome.lower transforma toda a string em minuscula , isso elimina erros caso tenha letras maiusculas