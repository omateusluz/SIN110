# Importação de bibliotecas e/ou arquivos
import Processamento as p
import Entrada as e
import Saida as s

# Função principal
if __name__ == '__main__':

    # Loop para automatizar os testes
    for i in range(3):

        # Condicional para definir
        # qual arquivo será aberto
        if i == 0:
            nome = 'exemplo'

        elif i == 1:
            nome = 'ponte'

        else:
            nome = 'zachary'

        # 'matriz' é a matriz que será
        # obtida a partir da função de entrada
        matriz = e.entrada(nome)

        # A função obtêm a quantidade de linhas
        # e a quantidade de colunas da matriz,
        # exibe as dimensões obtidas na tela e
        # retorna estes valores
        linhas, colunas = p.processamento(nome, matriz)

        # A função 
        s.saida(nome, linhas, colunas)