#while para validação

primeira = int(input('Primeiro bimestre: '))
while primeira > 10:
    primeira = int(input('Você digitou errado. Primeiro bimestre: '))
segunda = int(input('Segundo bimestre: '))
while segunda > 10:
    segunda = int(input('Você digitou errado. Segundo bimestre: '))
terceira = int(input('Terceiro bimestre: '))
while terceira > 10:
    terceira = int(input('Você digitou errado. Terceiro bimestre: '))
quarta = int(input('Quarto bimestre: '))
while quarta > 10:
    quarta = int(input('Você digitou errado. Quarto bimestre: '))
media1 = (primeira + segunda + terceira + quarta) / 4

print('Média: {}'.format(media1))
