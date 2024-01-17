velocidade = float(input('Digite a velocidade que você estava dirigindo:'))
if velocidade > 80:
    n1 = velocidade - 80
    n2 = n1 * 7
    print('Você foi multado por ultrapassar os limites de velocidade')
    print('O valor da sua multa é de R${}' .format(n2))
else:
    print('A sua velocidade está dentro do permitdo!')