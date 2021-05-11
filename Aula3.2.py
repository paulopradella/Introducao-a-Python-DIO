#Operdores condicionaas e lógicos:
d = int(input('Entre com o primeiro valor'))
e = int(input('Entre com o segundo valor'))

resto_a = d % 2
resto_b = e % 2

if resto_a == 0 or not resto_b > 0:
    print('Foi digitado um número par')
else:
    print('Nenhum número é par')
