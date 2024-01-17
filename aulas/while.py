'''x = 1 
while x < 11:
    print(x)
    x = x+1
print('fim do programa')'''


nome = input('Digite o nome:')
nome_desejado = 'Arthur'
while nome != nome_desejado:
    print('Este não é o nome correto')
    nome = input('Digite o nome novamente:')
print('Nome inserido está correto!')