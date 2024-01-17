valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Digite o valor do seu salario: R$'))
anos_pagamento = int(input('Em quantos anos você gostaria de pagar a casa?'))
valor_prestação = valor / (anos_pagamento *12)
calculo = salario * 30/100
print('Para comprar a casa de {:.2f} em {} anos' .format(valor, anos_pagamento))
print('O valor da sua prestação será de: R${:.2f}' .format(valor_prestação))
if calculo <= valor_prestação:
    print('Você não pode comprar esta casa pois o valor ultrapassa os 15%')
else:
    print('Compra concedida!')

