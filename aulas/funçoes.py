def fazer_um_big_mac(nome):
    print(f'fazer Big Mac {nome}')

def batata_frita(tamanho):
    print(f'fazer batata {tamanho}')

def bebida(tipo, tamanho):
    print(f'{tipo} {tamanho}')


def fazer_o_combo(nome_cliente, tamanho_batata, tipo_bebida, tamanho_bebida ):
    fazer_um_big_mac(nome_cliente)
    batata_frita(tamanho_batata)
    bebida(tipo_bebida, tamanho_bebida)

fazer_um_big_mac('Arthur')
batata_frita('Grande')
bebida('Coca-cola', '500ml')

print('Obrigado pela preferencia!')
r = input('Gostaria de fazer alguma reclamação? digite sim ou não. ')
if r == 'sim':
    input('faça aqui sua reclamaçaõ:')
    print('obrigado pelo seu feedback!')
else:
    print('Muito obrigado, volte sempre!')


