from datetime import date 
ano = int(input('Digite um ano para verificar se ele é bissexto. Para saber se o seu ano atual é bissexto digite:00///'))
if ano == 00:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano %400 == 0:
    print('Este ano é bissexto')
else:
    print('O ano digitado nao é considerado bissexto')
