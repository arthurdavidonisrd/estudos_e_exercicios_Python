tabela_brasileirao =('botafogo', 'flamengo', 'palmeiras', 'gremio', 'fluminense', 'bragantino', 'Athletico-pr', 'sao paulo','cuaiaba', 'cruzeiro', 'fortaleza', 'internacional', 'atletico-mg', 'corinthians', 'santos', 'goias', 'bahia', 'coritiba', 'america-mg', 'vasco da gama')

print('Os cinco primeiros são: {}' .format(tabela_brasileirao[0:5]))
print('=' *25)
print('Os quatro ultimos colocados são: {}' .format(tabela_brasileirao[16:]))
print('=' *25)
print('Os times em ordem alfabética são: {}' .format(sorted(tabela_brasileirao)))
print('=' *25)
print('O time do São Paulo está na {}ª posição' .format(tabela_brasileirao.index('sao paulo')+1))