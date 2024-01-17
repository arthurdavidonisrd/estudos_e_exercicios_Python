soma_de_idade = 0
mediaidade = 0 
for p in range(1,5):
    print('========={}ª PESSOA========' .format(p))
    nome = input('Digite seu nome:').strip()
    idade = int(input('Digite sua idade:'))
    sexo = input('Seu sexo: [M/F]').strip()
    soma_de_idade = soma_de_idade + idade 

mediaidade = soma_de_idade /4
