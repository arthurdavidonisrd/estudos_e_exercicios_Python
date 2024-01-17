#exercicio que leia quanto de dinheiro ela tem na carteira e quantos dolares ela pode comprar com esse dinheiro.
#cotação atual: 4,81

carteira = float(input('Quanto dinheiro voce tem na carteira? R$'))
conversao_dolar = carteira / 4.81
print('Você pode comprar U${:.2f} com o seu valor de R${:.2f} ' .format(conversao_dolar, carteira))