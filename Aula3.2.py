#Operdores condicionaas e lógicos:
nota1 = int(input('Primeiro bimestre: '))
nota2 = int(input('Segundo bimestre: '))
nota3 = int(input('Terceiro bimestre: '))
nota4 = int(input('Quarto bimestre: '))

media = (nota1 + nota2 + nota3+ nota4) / 4
if nota1 <= 10 and nota2 <= 10 and nota3 <= 10 and nota4 <= 10:
    print('Média: {}'.format(media))
else:
    print('foi informada alguma nota errada')

