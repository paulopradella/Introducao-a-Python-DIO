#Operdores condicionaas e lógicos:
a = int(input('Primeiro valor'))
b = int(input('Segundo valor'))
c = int(input('Terceiro valor'))

if a > b and a > c:
    print('O maior número é {}'. format(a))
elif b > a and b > c:
    print('O maior número é {}'.format(b))
else:
    print('O maior número é {}'.format(c))
print('Final do programa')

