#Gerenciando e criando exceções customizadas com try, except, else e finally

#forçar um erro
# divisao = 10 / 0#retorna: ZeroDivisionError: division by zero

try:#tudo que estiver dentro vai ser tratado na exceção
    divisao = 10 / 1
except ZeroDivisionError:
    print('Não é possível relizar uma divisão por zero')