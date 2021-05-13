#Gere, copie, mova, escreva e leia informações de
# arquivos externos
import shutil
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
    arquivo = open(nome_arquivo, 'a')
    #para escrever no arquivo:
    arquivo.write(texto)
    #Para fechar o arquivo
    arquivo.close()

def ler_arquivo(nome_arquivo):
    #Possibilita a leitura o arquivo
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')#vai criar uma lista, cada vez q encontrar
    #o argumento passado, vai criar um novo item na lista
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

#mover e copiar
#copiar
def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '/Users/paulo.pradella/OneDrive/Introducao-a-Python-DIO/')

#mover
def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '/Users/paulo.pradella/OneDrive/Introducao-a-Python-DIO/')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    #escreve_arquivo('Primeira Linha.\n')
    #aluno = 'Cesar, 7, 9 3, 8\n'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')