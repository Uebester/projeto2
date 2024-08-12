# pecorrer todos os arquivos da pasta de dados (pasta vendas)
import os
import pandas as pd
import plotly.express as px # bliblioteca que cria grafico

lista_arquivo = os.listdir("C:\\Users\\uebes\\Downloads\\Vendas-20240810T122054Z-001\\Vendas")

# tabela vazia
tabela_total = pd.DataFrame()

# passo 2 -importar as bases de dados de vendas
for arquivo in lista_arquivo:
     # se tem "vendas" no nome do arquivo, então
 if "Vendas" in arquivo:
      #importar base de dados
    tabela =  pd.read_csv(f"C:\\Users\\uebes\\Downloads\\Vendas-20240810T122054Z-001\\Vendas\\{arquivo}")
    tabela_total = tabela_total._append(tabela)
    
    # passo 3 tratar / compilar as bases de dados
    print(tabela_total)
    
    #passo 4 calcular o produto mais vendidos (em qunatidade)      sort_values(by="",ascending=false) = para ordenar os valores do maior para o menor
    tabela_produtos =tabela_total.groupby("Produto").sum()
    tabela_produtos = tabela_produtos [["Quantidade Vendida",]].sort_values(by="Quantidade Vendida", ascending=False)
    print(tabela_produtos)
    
    # passo 5 - calcular o produto que mais faturou (em faturamentos)
    tabela_total ["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]
    
    tabela_faturamento = tabela_total.groupby("Produto").sum()
    tabela_faturamento = tabela_faturamento [["Faturamento",]].sort_values(by="Faturamento", ascending=False)
    print(tabela_faturamento)
    
    # passo 6 calcular a loja/cidade que mais vendeu (faturamento)- criar um grafico/ dashboard
tabela_lojas = tabela_total.groupby("Loja").sum()
tabela_lojas =tabela_lojas[["Faturamento"]]
print(tabela_lojas)

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y="Faturamento")
grafico.show()