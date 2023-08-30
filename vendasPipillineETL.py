import pandas as pd

# Passo de Extração
def extrair_dados_vendas(arquivo_vendas):
    dados_vendas = pd.read_csv(arquivo_vendas)
    return dados_vendas

def extrair_dados_estoque(arquivo_estoque):
    dados_estoque = pd.read_csv(arquivo_estoque)
    return dados_estoque

# Passo de Transformação
def transformar_dados(dados_vendas, dados_estoque):
    # Realizar junção dos dados de vendas e estoque com base no ID do produto
    dados_combinados = pd.merge(dados_vendas, dados_estoque, on='ID_Produto')

    # Calcular o valor total de cada venda (Quantidade * Preço)
    dados_combinados['Valor_Total'] = dados_combinados['Quantidade'] * dados_combinados['Preco']

    return dados_combinados

# Passo de Carregamento
def carregar_dados(dados_transformados, caminho_saida):
    dados_transformados.to_csv(caminho_saida, index=False)

def main():
    arquivo_vendas = 'dados_vendas.csv'
    arquivo_estoque = 'dados_estoque.csv'
    arquivo_saida = 'relatorio_consolidado.csv'

    # Etapa de Extração
    dados_vendas = extrair_dados_vendas(arquivo_vendas)
    dados_estoque = extrair_dados_estoque(arquivo_estoque)

    # Etapa de Transformação
    dados_transformados = transformar_dados(dados_vendas, dados_estoque)

    # Etapa de Carregamento
    carregar_dados(dados_transformados, arquivo_saida)

if __name__ == '__main__':
    main()
