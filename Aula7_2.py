#Criando classe
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

calculadora = Calculadora(10, 2)#estanciar
if __name__ == '__main__':
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())

#Outra forma de fazer a calculadora usando classe
# # class Calculadora:
# #
# #     def soma(self,valor_a, valor_b):
# #         return valor_a + valor_b
# #
# #     def subtracao(self,valor_a, valor_b):
# #         return valor_a - valor_b
# #
# #     def multiplicacao(self,valor_a, valor_b):
# #         return valor_a * valor_b
# #
# #     def divisao(self,valor_a, valor_b):
# #         return valor_a / valor_b
#
#
# calculadora = Calculadora()
# if __name__ == '__main__':
#     print(calculadora.soma(10, 2))
#     print(calculadora.subtracao(5, 3))
#     print(calculadora.multiplicacao(10, 5))
#     print(calculadora.divisao(100, 2))
