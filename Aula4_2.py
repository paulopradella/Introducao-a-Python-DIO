#Descobrir se é primo for/range
a = int(input('Entre com um número'))

div = 0
for z in range(1, a +1):
    resto = a % z
    print(z, resto)
    if resto == 0:
        div += 1
if div == 2:
    print('Número {} é primo' .format(a))
else:
    print('Número {} não é primo'.format(a))
