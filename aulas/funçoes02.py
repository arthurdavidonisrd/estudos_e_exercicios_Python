doce = int(5.00)
pao_de_mel = int(50.00)
bebes = int(6.00)
def fazer_doce(nome, tipo):
    print(nome, tipo)

def fazer_pao_de_mel(quantidade):
    print(f'fazer {quantidade} de pão de mel' )

def bebida(tipo, tamanho):
    print(f'{tipo}, {tamanho}')

fazer_doce('Arthur', 'doce de nozes')
fazer_pao_de_mel('50 unidades')
bebida('Coca-cola', '500ml')

valor = bebes + pao_de_mel + doce
print('O valor do seu pedido é de R$ {} !'.format(valor))

feed = input('Você tem alguma reclamação para fazer do seu pedido? Digite Sim ou Não:')
if feed == 'Sim':
    input('Envie aqui sua reclamação:')
    print('Agradecemos o seu feedback, e pedimos desculpas por qualquer incomodo!')
else:
    print('Obrigado pela sua compra! Volte sempre')



