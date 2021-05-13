#Gerenciando e criando exceções customizadas com try, except, else e finally

#forçar um erro
# divisao = 10 / 0#retorna: ZeroDivisionError: division by zero
lista = [1, 10]
try:#tudo que estiver dentro vai ser tratado na exceção
    divisao = 10 / 1
    numero = lista[1]
    #x = x
#Encadeamento de exceção
except ZeroDivisionError:
    print('Não é possível relizar uma divisão por zero')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:#pega a exceçao de base.
    #É útil para tratar um erro ainda não previsto
    print('Erro desconhecido. Erro: {}'.format(ex))
else:#para cso não ocorra nenhum erro
    print('Executa quando não ocorrer exceção')