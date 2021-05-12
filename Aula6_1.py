#Organizando conjuntos e subconjuntos de elementos em Python:
#é criado usando chaves, caso possua dois elementos iguais ele imprime um apenas
conjunto = {1, 2, 3, 4, 4, 2}
print('O conjunto é: {}' .format(conjunto))
#adicionar eleentos ao conjunto
conjunto.add(5)
print('Adicionando ao conjunto é: {}' .format(conjunto))
#adicionar elementos ao conjunto
conjunto.discard(2)
print('Removendo do conjunto é: {}' .format(conjunto))
#união de dois conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2= {5, 6, 7, 8}
conjunto_uniao = conjunto1.union(conjunto2)
print('União: {}' .format(conjunto_uniao))
#intersecção
conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Intersecção: {}' .format(conjunto_interseccao))
#diferença
conjunto_diferenca1 = conjunto1.difference(conjunto2)
print('Diferença entre 1 e 2: {}' .format(conjunto_diferenca1))#resultado: 1,2,3,4
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print('Diferença entre 2 e 1: {}' .format(conjunto_diferenca2))#resultado: 8,6,7
#Diferença simétrica (tudo que não tem nos dois)
conjunto_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simétrica: {}' .format(conjunto_simetrica))#resultado: 1, 2, 3, 4, 6, 7, 8

