#Pertinência são os métodos de subset e superset: aqui é booleana
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
#Se é subconjunto:
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_subset))#resultado True
conjunto_subset1 = conjunto_b.issubset(conjunto_a)
print('B é subconjunto de A: {}'.format(conjunto_subset1))#resultado False
#Se é um super conjunto:
conjunto_superset = conjunto_a.issuperset(conjunto_b)
print('A é super conjunto de B: {}'.format(conjunto_superset))#resultado False
conjunto_superset1 = conjunto_b.issuperset(conjunto_a)
print('B é super conjunto de A: {}'.format(conjunto_superset1))#resultado True