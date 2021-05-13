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
#Busca informções sobre um pokemon
def retorna_dados_pokemon(pokemon):
    response = requests.get('http://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon
#retorno de um site normal
def retorna_response(url):
    response = requests.get(url)
    return response.text
if __name__ == '__main__':
    retorna_dados_cep('80230020')
    dados_pokemon = retorna_dados_pokemon('pikachu')
    print(dados_pokemon['sprites']['front_shiny'])
    response = retorna_response('http://globllabs.aacademy/')
    print(response)
