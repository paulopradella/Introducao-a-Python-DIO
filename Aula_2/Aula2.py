a = int(input('Entre com o primeiro valor'))
b = int(input('Entre com o segundo valor'))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
print('Soma: ', soma)
print('Soma: ' + str(soma))#convertendo em string
print('Soma: {}'.format(soma))#Concatenando com o format, indiferente do tipo de dado
print('Subtração: ', subtracao)
print('Multiplicação: ', multiplicacao)
print('Divisão: ', divisao)
print('Divisão: ', int(divisao))#convertendo para inteiro
print('Resto: ', resto)
print('soma: {}. Subtração: {}'.format(soma, subtracao))#Imprimir mais de uma variável usando o format
print('Soma: {soma}. '
      '\nSubtração: {sub}'
      '\nMultiplicação {Multiplicacao}'
      '\nDivisão {divisao}'
      '\nResto {resto}'.format(soma = soma,
                              sub = subtracao,
                              Multiplicacao = multiplicacao,
                              divisao = divisao,
                              resto = resto))#Outra forma de usar o format, aqui não importa a ordem
resultado = ('Soma: {soma}. '
      '\nSubtração: {sub}'
      '\nMultiplicação {Multiplicacao}'
      '\nDivisão {divisao}'
      '\nResto {resto}'.format(soma = soma,
                              sub = subtracao,
                              Multiplicacao = multiplicacao,
                              divisao = divisao,
                              resto = resto))# pode ser colocado dentro de uma variavel e imprimir ela
print(resultado)
# x = '1'
# soma2 = int(x) + 1
# print(soma2)