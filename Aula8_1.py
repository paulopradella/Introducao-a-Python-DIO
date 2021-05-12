#Lidando com módulos, importação de classes, métodos e
# construção de funções anônimas (lambda)
#Ex1.:
# >>>	import Aula7_3(tirar os prints
# >>>	 televisao = Aula7_3.Televisao()
# >>>	 televisao.ligada
# False
# >>>	 televisao.power()
# >>>	 televisao.ligada
# True
# Ex2.:Outras forma de acessar um módulo:
# >>>	from Aula8_1 import Televisão
# #Está falando que lá da Aula8_1 morte Televisao
# >>>	televisao = Televisao()
# >>>	 televisao.ligada
# False
# >>>	 televisao.power()
# >>>	 televisao.ligada
# True

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1


if __name__ == '__main__':
    #Qundo quem está chamando, se for o mesmo arquivo eu faço isso
    #se não, não faz nada, sempre que tiver que fazer testes, vai usar isso.
    #ou seja se estiver sendo executado o própria aquivo,
    # ele vai executar, caso contrário não
    televisao = Televisao()
    print('Televisão está ligada: {}' .format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}' .format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada: {}' .format(televisao.ligada))
    print('Canal: {}' .format(televisao.canal))
    televisao.power()
    print('Televisão está ligada: {}' .format(televisao.ligada))
    print('Canal: {}' .format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}' .format(televisao.canal))
    televisao.diminui_canal()
    print('Canal: {}' .format(televisao.canal))
