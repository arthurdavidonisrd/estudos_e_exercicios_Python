v = int(input('A que velocidade você estava dirigindo?'))
if v >=60:
    print('Você foi multado por ultrapassar o limite de veolocidade')
    print('O valor da multa é de 10 reais por km acima da média')
    m = v*10
    print('O valor da sua multa é de R$ {} '.format(m))
else:
    print('sua velocidade esta na média da rodovía')