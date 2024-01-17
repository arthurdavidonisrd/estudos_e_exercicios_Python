a = int(input('Digite o primeiro valor'))
b = int(input('Digite o segundo valor'))
c = int(input('Digite o terceiro valor'))
menor = b
if a<b and a<c:
    menor = a
if c<a and c<b:
    menor = c

maior = a 
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O maior número é: {}' .format(maior))
print('O menor número é: {}' .format(menor))