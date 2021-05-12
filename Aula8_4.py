#lambda (função anônima, é uma forma de simplificar algo que
# será utilizado mais de uma vez no código
#é mais eficiente com coisas que se resolve com uma linha,
#para coisa mais complexas não é bom

contador_letras = lambda lista:[len(x) for x in lista]
#vai fazer  mesma coisa do outro contdor, masfica mais simples no código

lista_animais = ['cachorro', 'gato', 'elefante']
total_letras = contador_letras(lista_animais)
print(total_letras)

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b

print(soma(5, 10))
print(subtracao(5, 10))
print(multiplicacao(5, 10))
print(divisao(5, 10))

#criar um dicionário com lambda

calculadora = {
   'soma': lambda a, b: a + b,
   'subtracao': lambda a, b: a - b,
   'multiplicacao': lambda a, b: a * b,
   'divisao': lambda a, b: a / b
}

soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']
print('A soma é: {}'.format(soma(5, 10)))
print('A subtração é: {}'.format(subtracao(5, 10)))
print('A multiplicaçao é: {}'.format(multiplicacao(5, 10)))
print('A divisão é: {}'.format(divisao(5, 10)))

