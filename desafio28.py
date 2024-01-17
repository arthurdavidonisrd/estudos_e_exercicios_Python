from random import randint
print('Vamos fazer um jogo de adivinhação')
computador = randint(0,5)
jogador = int(input('Digite um numero de 0 a 5:'))
if jogador == computador:
    print('Você acertou o número:')
else:
    print('Você perdeu!')

