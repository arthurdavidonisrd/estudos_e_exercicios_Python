from random import randint
computador = randint(0,5)
print('vamos jogar um jogo de adivinhação')
jogador = int(input('tente adivinhar o número que o computador esta pensando '))
if jogador == computador:
    print('Você me venceu')
else:
    print('Você errou o numero!')