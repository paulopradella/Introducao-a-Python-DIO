#soma de valores de uma lista
lista_inteiros = [12, 10, 7, 5]
lista_animal =['cachorro', 'gato', 'elefante']

soma = 0
for x in lista_inteiros:#vai percorer a lista
    print(x)
    soma += x
print(soma)

print(sum(lista_inteiros))#vai imprimir a soma da lista por isso sempre usar o mesmo tipo
