nome = input('Digite seu nome:').strip()
idade = int(input('Digite sua idade:'))
if nome == 'Arthur' and idade == 17:
    print('Está correto, acesso concedido')
elif nome == 'Eduarda' or nome == 'Carla' or nome == 'João':
    print('Acesso também concedido')
else:
    print('Acesso negado!')