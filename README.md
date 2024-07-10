# Projeto - Automação de Tarefas
## Descrição
Este projeto realiza a automação de tarefas dentro do navegador web (Google Chrome). 

## Funcionalidades
- Abrir o navegador Google Chrome
- Entrar no sistema
- Fazer login com credenciais fornecidas pelo usuário
- Importar produtos de um arquivo CSV
- Cadastrar produtos no sistema

## Estrutura do Projeto
- `Navegador.py`: Contém a classe `Navegador` responsável por interagir com o navegador web.
- `Usuario.py`: Contém a classe `Usuario` para armazenar as credenciais do usuário.
- `Produto.py`: Define a classe `Produto` para representar os produtos a serem cadastrados.
- `Importacao.py`: Contém a classe `Tarefas` que importa produtos de um arquivo CSV.
- `main.py`: Script principal que integra todas as funcionalidades para executar a automação.

## Arquivos

### `main.py`
```python

from Navegador import Navegador
from Usuario import Usuario
from Importacao import Tarefas

navegador = Navegador()
usuario = Usuario()
tarefas = Tarefas()

navegador.abrir_navegador()
navegador.entrar_sistema()
navegador.fazer_login(usuario.obter_login(), usuario.obter_senha())
lista_produtos = tarefas.importar_produtos()
navegador.cadastro_produtos(lista_produtos)

### `Navegador.py`
```python

import pyautogui
import time
from Importacao import Tarefas 
from Produto import Produto 

pyautogui.PAUSE = 2 

class Navegador:
    def __init__(self):
        pass 

    def abrir_navegador(self): 
        pyautogui.press('win')
        pyautogui.write('chrome')
        pyautogui.press('enter') 
        
    def entrar_sistema(self):
        pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
        pyautogui.press('enter') 
        time.sleep(3) 

    def fazer_login(self, email, senha):
        pyautogui.press('tab')
        pyautogui.write(email)
        pyautogui.press('tab')
        pyautogui.write(senha)
        pyautogui.press('enter')
        time.sleep(3) 

    def cadastro_produtos(self, lista_produtos): 
        for produto in lista_produtos: 
            pyautogui.press('tab') 
            pyautogui.write(produto.codigo)
            pyautogui.press('tab')
            pyautogui.write(produto.marca)
            pyautogui.press('tab') 
            pyautogui.write(produto.tipo)
            pyautogui.press('tab')
            pyautogui.write(produto.categoria)
            pyautogui.press('tab') 
            pyautogui.write(produto.preco_unitario)
            pyautogui.press('tab')
            pyautogui.write(produto.custo)
            pyautogui.press('tab')
            pyautogui.write(produto.obs) 
            pyautogui.press('enter')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab') 
            time.sleep(3) 
            pyautogui.scroll(5000)

### `Usuario.py`
```python

class Usuario:
    def __init__(self):
        pass

    def obter_login(self):
        return 'leomarino1999@gmail.com'

    def obter_senha(self):
        return 'LeoProjetoAutomacao'

### `Produto.py`
```python

class Produto:
    def __init__(self, codigo, marca, tipo, categoria, preco_unitario, custo, obs):
        self.codigo = codigo
        self.marca = marca
        self.tipo = tipo
        self.categoria = categoria
        self.preco_unitario = preco_unitario
        self.custo = custo
        self.obs = obs

### `Importacao.py`
```python

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

## Requisitos
- pyautogui
- pandas
- os 
