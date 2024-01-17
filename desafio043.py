p = float(input('Qual é seu peso? Kg'))
a = float(input('Qual a sua altura? m'))
imc = p / (a ** 2)
if imc < 18.5:
    print('Seu indice de massa corporal é de {}' .format(imc))
    print('Você está abaixo do peso')
elif imc > 40:
    print('Seu indice de massa corporal é de {}' .format(imc))
    print('Obesidade mórbida')
elif 18.5 <= imc < 25:
    print('Seu indice de massa corporal é de {}' ,format(imc))
    print('Você está no peso ideal')
elif 25 <= imc < 30:
    print('Você está com sobrepeso')
elif 30 <= imc < 40:
    print('Seu indice de massa corporal é de {}' .format(imc))
    print('Você está em situação de obesidade')