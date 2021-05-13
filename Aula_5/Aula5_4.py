#Validar se um valor existe na lista usando condicional
lista_inteiros = [12, 10, 7, 5]
lista_animal =['cachorro', 'gato', 'elefante']
if 'gato' in lista_animal:
    print('existe um gato na lista')
else:
    print('não existe um gato na lista')
#Validar se um valor existe na lista usando condicional e incluir novo elemento
if 'lobo' in lista_animal:
    print('existe um lobo na lista')
else:
    print('não existe um lobo na lista. Será incluido')
    lista_animal.append('lobo')#inclui após o ultimo elemento já existente
    print(lista_animal)