km = float(input('Quantos quilometros você andou com esse carro?'))
dias = int(input('Por quantos dias você alugou este carro?'))
valor1 = 0.15 * km
valor2 = 60 * dias
print('O valor do carro por quilometros rodados é de R${:.2f}'.format(valor1))
print('O valor do carro por dias alugados é de R${:.2f}'.format(valor2))
valor_final = valor1 + valor2
print('O valor final do seu aluguel é de R${:.2f}'.format(valor_final))
