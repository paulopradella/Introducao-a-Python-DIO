#Gere, copie, mova, escreva e leia informações de
# arquivos externos

def escreve_arquivo(texto):
    #Criar arquivos:
    arquivo = open('teste.txt', 'w')
    #para escrever no arquivo:
    arquivo.write(texto)
    #Para fechar o arquivo
    arquivo.close()

def atualizar_arquivo(texto):
    #Adicionar ao arquivo existente e também criar um novo arquivo:
    arquivo = open('teste.txt', 'a')
    #para escrever no arquivo:
    arquivo.write(texto)
    #Para fechar o arquivo
    arquivo.close()

def ler_arquivo(nome_arquivo):
    #Possibilita a leitura o arquivo
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    #escreve_arquivo('Primeira Linha.\n')
    #atualizar_arquivo('Segunda linha.\n')
    ler_arquivo('teste.txt')