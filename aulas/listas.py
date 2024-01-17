#LISTAS EM PYTHON
#as listas são definidas por: []
#As listas são MUTAVEIS
#======================PARA ADICIONAR INTES NA LISTA===========================
#lanche.append('....') -serve para adicionar novos elementos na lista
#lanche.insert('.....') -para adiocinar um item no começo da lista, ou seja na posição zero(fazendo isso todos os itens trocam de numeração)
#======================PARA REMOVER ITENS DA LISTA=============================
#lanche.pop(x) -serve para eliminar o ultimo elemento
#del lanche(y)
#lanche.remove('nome do lanche)
#======================PARA COLOCAR ELEMENTOS EM ORDEM=========================
#valores.sort()
#valores.sort(reverse=True)

#valores = list(range(4,11))
#print(valores)

valores = []
valores.append(2)
valores.append(4)
valores.append(6)
valores.append(8)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')