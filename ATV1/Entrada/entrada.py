# Importação de bibliotecas e/ou arquivos
import numpy as np

# A função abre o arquivo cujo nome é
# parâmetro, lê o conteúdo e retorna
# uma matriz numpy como resposta
def entrada(nome):

    # Armazena a localização do arquivo
    local = 'Data/' + nome + '.txt'

    # Abre o arquivo para leitura ('r')
    arquivo = open(local, 'r')

    # A função 'loadtxt' armazena os dados
    # do arquivo na matriz Numpy
    matriz = np.loadtxt(arquivo)

    # Fecha o arquivo
    arquivo.close

    # Retorna a matriz
    return matriz