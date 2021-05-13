#Gerenciando e criando exceções customizadas com try, except, else e finally
#Exceção personalizada
class Error(Exception):#Obrigatória para criar uma classe e erro personalizada
    pass

#personalizada
class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10')
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Vaor inválido, deve-se digitar apenas números')
    except InputError as ex:
        print(ex)
