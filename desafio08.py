valor_metros = int(input('Digite o valor em metros que deseja:'))
print('Você escolheu {} metros de comprimento' .format(valor_metros))
valor_cm = valor_metros * 100
valor_mm = valor_metros * 1000
print('O valor convertido para centimetros fica: {}'.format(valor_cm))
print('O valor convertido para milimetros fica: {}'.format(valor_mm))