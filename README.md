# Pipeline ETL para Relatório Consolidado de Vendas e Estoque

Este projeto consiste em uma pipeline ETL (Extração, Transformação e Carregamento) desenvolvida em Python, que tem como objetivo criar um relatório consolidado de vendas e estoque a partir de dados brutos de diferentes fontes. A pipeline realiza a extração dos dados de vendas e estoque de arquivos CSV, realiza a transformação dos dados, incluindo a combinação de informações e o cálculo do valor total das vendas, e, finalmente, carrega o relatório consolidado em um novo arquivo CSV.

## Funcionalidades

- **Extração de Dados:** Os dados brutos de vendas e estoque são extraídos de arquivos CSV separados.
- **Transformação de Dados:** Os dados de vendas e estoque são combinados com base no ID do produto. O valor total de cada venda é calculado multiplicando a quantidade pelo preço unitário.
- **Carregamento de Dados:** O relatório consolidado é carregado em um arquivo CSV.

## Arquivos do Projeto

- `main.py`: Contém o código principal da pipeline ETL, incluindo as funções de extração, transformação e carregamento.
- `dados_vendas.csv`: Exemplo fictício de dados de vendas.
- `dados_estoque.csv`: Exemplo fictício de dados de estoque.
- `relatorio_consolidado.csv`: Arquivo de saída com o relatório consolidado de vendas e estoque.

## Requisitos

- Python 3.x
- Biblioteca pandas

## Instruções de Uso

1. Certifique-se de ter Python 3.x instalado.
2. Instale a biblioteca pandas executando `pip install pandas`.
3. Edite os arquivos `dados_vendas.csv` e `dados_estoque.csv` com seus próprios dados, se necessário.
4. Execute o arquivo `main.py` para iniciar a pipeline ETL e gerar o relatório consolidado.

## Observações

Este projeto é um exemplo simplificado de uma pipeline ETL e pode ser adaptado e estendido para atender a necessidades específicas. Consulte a documentação da biblioteca pandas para mais informações sobre manipulação de dados e outras funcionalidades.
