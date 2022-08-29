# A função obtêm a quantidade de linhas
# e a quantidade de colunas da matriz
# passada como parâmetro, depois exibe
# no console e retorna os valores
def processamento(nome, matriz):
    
    # Armazena a quantidade
    # de linhas da matriz
    linhas = len(matriz[0])

    # Armazena a quantidade
    # de colunas da matriz
    colunas = len(matriz)

    # Exibe os valores
    print(nome + ' (' + str(linhas) + ', ' + str(colunas) + ')' + '\n')

    return linhas, colunas