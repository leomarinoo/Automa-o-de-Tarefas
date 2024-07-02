from Produto import Produto
import pandas as pd
import os

class Tarefas:
    def __init__(self): 
        self.produtos = []

    def importar_produtos(self):
        tabela = pd.read_csv(os.getcwd() + "/produtos.csv")
        print(tabela) 

        for _, linha in tabela.iterrows(): 

            produto = Produto(
                codigo=str(linha["codigo"]),
                marca=str(linha["marca"]),
                tipo=str(linha["tipo"]),
                categoria=str(linha["categoria"]),
                preco_unitario=str(linha["preco_unitario"]),
                custo=str(linha["custo"]),
                obs=str(linha["obs"]) if not pd.isna(linha["obs"]) else "") 
            self.produtos.append(produto) 
        
        return self.produtos 

tarefas = Tarefas()
lista_produtos = tarefas.importar_produtos() 