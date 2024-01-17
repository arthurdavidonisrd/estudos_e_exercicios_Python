from datetime import date
ano = int(input('Qual o ano de nascimeto do atleta?'))
atual = date.today().year
idade = atual - ano
print('O atleta nasceu no ano de {}' .format(ano))
print('O atleta tem {} anos' .format(idade))
if idade <= 9:
    print('O atleta está na categoria MIRIM')
elif idade <= 14:
    print('O atleta está na categoria INFANTIL')
elif idade <= 19:
    print('O alteta está na categoria JUNIOR')
elif idade <= 25:
    print('O atleta está na categoria SÊNIOR')
else:
    print('O atleta faz parte da categoria MASTER')