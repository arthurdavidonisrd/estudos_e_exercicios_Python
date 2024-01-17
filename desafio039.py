from datetime import date
atual = date.today().year
idade = int(input('digite sua idade: '))
nascimento = atual - idade
print('Quem nasceu em {} tem {} anos em {}' .format(nascimento, idade, atual))
if idade == 18:
    print('Você está no ano do alistamento, corra imediatamente se alistar!!')
elif idade < 18:
    tempo = 18 - idade
    print('Ainda faltam {} ano(s) para o seu alistameto' .format(tempo))
elif idade > 18:
    tempo = idade - 18
    print('Você ja tem {} anos, deveria ter se alistado ja fazem {} ano(s) ' .format(idade, tempo ))
    ano = atual - tempo
    print('Seu alistamento deveira ter sido feito no ano de: {}' .format(ano))