sexo = input('Informe seu sexo: [M/F] ' ).upper().strip()
while sexo != 'M' and sexo != 'f':
    sexo = input('Dados invalidos, insira seu sexo novamente!')
print('Registro feito com sucesso')