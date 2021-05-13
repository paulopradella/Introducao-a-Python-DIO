#Instalando e utilizando pacotes em Python e
# realizar requisição com requests
import requests

def retorna_response(url):
    response = requests.get(url)
    return response.text
if __name__ == '__main__':
    response = retorna_response('http://globllabs.aacademy/')
    print(response)