import pyautogui
import time
import pandas as pd
import os

# comando "pyautogui.PAUSE" = tempo de execução/intervalo de um comando para o outro
pyautogui.PAUSE = 2

# Criando classe "Tarefas"
class Tarefas:
    def __init__(self):
        self.tabela = None

# metodo 1 - Abrir/Importar a base de produtos para cadastrar
    def importar_produtos(self):
        self.tabela = pd.read_csv(os.getcwd()+ "/produtos.csv")  
        print(self.tabela) 

# metodo 2 - Cadastrar um produto
    def cadastrar_produto(self):

        for linha in self.tabela.index:
            codigo = str(self.tabela.loc[linha, "codigo"])

    # clicar no campo de código
            pyautogui.click(x=422, y=296) 

    # pegar da tabela o valor do campo que a gente quer preencher
            codigo = self.tabela.loc[linha, "codigo"]

    # preencher o campo
            pyautogui.write(str(codigo))

    # passar para o proximo campo
            pyautogui.press("tab")

    # preencher o campo
            pyautogui.write(str(self.tabela.loc[linha, "marca"]))
            pyautogui.press("tab")
            pyautogui.write(str(self.tabela.loc[linha, "tipo"]))
            pyautogui.press("tab")
            pyautogui.write(str(self.tabela.loc[linha, "categoria"]))
            pyautogui.press("tab")
            pyautogui.write(str(self.tabela.loc[linha, "preco_unitario"]))
            pyautogui.press("tab")
            pyautogui.write(str(self.tabela.loc[linha, "custo"]))
            pyautogui.press("tab")
            obs = self.tabela.loc[linha, "obs"]
            if not pd.isna(obs):
                pyautogui.write(str(self.tabela.loc[linha, "obs"]))
            pyautogui.press("tab")
            pyautogui.press("enter") 

    # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
            pyautogui.scroll(5000)

    # metodo 3 - Repetir o processo de cadastro dos produtos até o final 