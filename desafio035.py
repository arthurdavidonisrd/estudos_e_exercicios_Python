r1 = float(input('Informe o tamanho do primeiro segmento:'))
r2 = float(input('Informe o tamanho do segundo segmento:'))
r3 = float(input('Informe o tamanho do terceiro segmento:'))
if r1 < r2 + r3 and  r2 < r1 + r3 and r3 < r2 + r1:
    print('É possivel fazer um triangulo')
else:
    print('Não é possivel fazer um triangulo')