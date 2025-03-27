def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')

    for linha in arquivo:
        print(linha)

    arquivo.close()


def salvar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto)
    arquivo.close()


ler_arquivo('pessoas.txt')
salvar_arquivo('testandoArquivo.txt', 'testando a escrita de um arquivo')
ler_arquivo('testandoArquivo.txt')
