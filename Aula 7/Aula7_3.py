#Fazer uma televisõo usando método e classe

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

televisao = Televisao()
print('Teleisão está ligada: {}' .format(televisao.ligada))
televisao.power()
print('Teleisão está ligada: {}' .format(televisao.ligada))
televisao.power()
print('Teleisão está ligada: {}' .format(televisao.ligada))
print('Canal: {}' .format(televisao.canal))
televisao.power()
print('Televisão está ligada: {}' .format(televisao.ligada))
print('Canal: {}' .format(televisao.canal))
televisao.aumenta_canal()
televisao.aumenta_canal()
print('Canal: {}' .format(televisao.canal))
televisao.diminui_canal()
print('Canal: {}' .format(televisao.canal))
