print('LOJA DO THUR')
print('-' * 70)
preço_compras = float(input('Digite o valor das suas compras: R$' ))
def pag():
    print('[1] à vista no dinheiro/cheque')
    print('[2] à vista no cartão')
    print('[3] 2x no cartão')
    print('[4] 3x ou mais no cartão')

forma_pag = int(input('Qual sua forma de pagamento?'))

if forma_pag == 1:
    print('Sua forma de pagamento será à vista no dinheiro/cheque')
    desconto10 = preço_compras - (preço_compras * 10 / 100)
    print('O valor da sua compra ficou R${} com o desconto de 10%'.format(desconto10))


elif forma_pag == 2:
    print('Sua forma de pagamento será à vista no cartão')
    desconto5 = preço_compras - (preço_compras * 5/100)
    print('Pagando R${} à vista no cartão você recebera um deconto de 5%, assim você pagara R${}'.format(preço_compras, desconto5))
    
elif forma_pag == 3:
    print('Sua forma de pagamento será em 2x no cartão')
    parcela = preço_compras/2
    print('Em 2x no cartão você não obteve desconto, o valor da sua compra é de R${}' .format(parcela))
    
elif forma_pag == 4:
    print('Sua forma de pagamento será em 3x ou mais no cartão')
    total  = preço_compras + (preço_compras * 20 / 100)
    parc = int(input('Quantas parcelas?'))
    parc2 = total / parc
    print('Sua compra no valor de R${} vai ser parcelada em {} parcelas '.format(preço_compras, parc, ))
    print('E o valor a pagar sera de R${}' .format(parc2))
    print('O valor total ao final será de R${}' .format(total))
else:
    print('=' *70)
    print('Opção de pagamento selecionada não existe!')
    print('Por favor, tente novamente.')
    
    
    



