#def mensagem(msg):
   # print('=' *30)
   # print(msg)
   # print('=' *30)

#mensagem('Sistema de alunos')


#def calc(a,b):
   # m = a+b
    #print(f'os valores são {a} somado com {b}')
   # print(f'E o resultado é igual a:{m}')

#calc(4,2)
#calc(2,2)
#calc(5,1)


#def contador(*num):
  # for valores in num:
  #    print(valores)


#contador(2,4,6,7)
#contador(2,4)
#contador(2)
#contador(2,3,8,5)
  



#def mult(a,b): #parametros que a função recebe!.
   # m = a*b
   # print(m)


#mult(4,2)
#mult(5,5)
#mult(2,2)


#====================================EMPACOTAMENTO DE PARAMETROS=====================================================================================================
#passar o * dentro dos parenteses, que diz ao python que varios parametros serão passados.


#def contador(*numeros):
    #print(numeros)
    

#contador(2,3,5,6)
#contador(2,7,1,0,8)
#contador(10,9,6)



def dobra(lst):
    pos = 0 
    while pos < len(lst):
        multi = lst[pos] * 2
        pos + 1




valores = [10,2,4,6,9]
dobra(valores)
print(valores)




