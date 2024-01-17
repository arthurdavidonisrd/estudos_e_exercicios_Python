n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota:' ))
soma = n1+n2
media = soma/2
if media <5.0:
    print('Você foi reprovado!')
    print('Sua média foi {:.1f}' .format(media))
elif media >= 7.0:
    print('Você foi aprovado!')
    print('Sua média foi {:.1f}' .format(media))
elif 7 > media >= 5  :
    print('Você ficou de recuperação!')
    print('Sua média foi {:.2f}' .format(media))
