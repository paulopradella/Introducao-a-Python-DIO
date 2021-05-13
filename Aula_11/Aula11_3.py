#Gerenciando e criando exceções customizadas com try, except, else e finally
#Tem um pedaço e códgo que indiferente de erro, precisa ser executado
lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 0#como tem esse erro, ele não continuou executndo
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possível relizar uma divisão por zero')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorrer exceção')
finally:#Sempre vai executar, mesmo que de erro
    print('Sempre executa')
    print('Fechando o arquivo')
    arquivo.close()