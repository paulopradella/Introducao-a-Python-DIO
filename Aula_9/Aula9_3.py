#Gere, copie, mova, escreva e leia informações de
# arquivos externos

def escreve_arquivo(texto):
    #Criar arquivos em um local determinado:
    diretorio = '/Users/paulo.pradella/OneDrive/Introducao-a-Python-DIO/Aula_9/teste.txt'
    #Cria o arquivo
    arquivo = open(diretorio, 'w')
    #para escrever no arquivo:
    arquivo.write(texto)
    #Para fechar o arquivo
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    #Adicionar ao arquivo existente e também criar um novo arquivo:
    arquivo = open('nome_arquivo', 'a')
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
    escreve_arquivo('Primeira Linha.\n')
    #aluno = 'Cesar, 7, 9, 3, 8\n'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')