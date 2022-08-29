def saida(nome, linhas, colunas):

    # Abre o arquivo para escrita ('a+')
    arquivo = open('Data/saida.txt', 'a+')

    # Faz a escrita no arquivo
    arquivo.write(nome + ' (' + str(linhas) + ', ' + str(colunas) + ')' + '\n')

    # Fecha o arquivo
    arquivo.close