#Instalando e utilizando pacotes em Python e
# realizar requisição com requests
import requests
#Buscar informções de um cep com o requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)#200 ok/400 Erro
    print(response.text)#traz como string
    print(response.json())#traz como dicioário
    dados_cep = response.json()#incerindo os dados com lista dentro da variavel
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

if __name__ == '__main__':
    retorna_dados_cep('22041001')