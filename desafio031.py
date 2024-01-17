distancia = float(input('Digite a distancia da sua viagem:'))
if distancia <= 200:
    calculo = distancia * 0.50
    print('O valor da sua passagem é R${}' .format(calculo))
else:
    calculo2 = distancia * 0.45
    print('Nesse caso o valor da sua passagem é de R${}'.format(calculo2))