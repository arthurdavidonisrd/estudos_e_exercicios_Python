print('='*30)
print('LISTAGEM DE PREÇOS')
print('='*30)
listagem = ('Lápis', 1.75,
           'Borracha', 2,
            'caderno', 15.90,
            'estojo', 25,
            'transferidor', 4.20,
            'compasso', 9.99,
            'mochila', 120.32,
            'canetas', 22.30,
            'livros', 34.90,)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos] :.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')





 