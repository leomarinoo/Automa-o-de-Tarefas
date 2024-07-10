# O projeto se baseia em cadastrar prudutos existentetes de uma base de dados em um sistema qualquer. 
# Automatizar o processo de cadastro dos produtos utilizando a biblioteca "pyautogui".

# PSEUDOCODIGO 
# 1- Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # pyautogui.write -> escrever um texto
    # pyautogui.press -> pressionar uma tecla do teclado
    # pyautogui.click -> clicar em algum lugar da tela com o mouse
    # pyautogui.hotkey -> combinação de teclas (CTRL C, CTRL V, ALT TAB) 

import pyautogui
import time

#Adicionar comando "pause" para que nenhum comando atropele o outro e não o execute
pyautogui.PAUSE = 3

# Abrir o navegador (Google Chorme)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# Entrar no sistema
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')


#biblioteca "time" para que o comando demore alguns segundos para carregar totalmente
time.sleep(6)

# 2- Fazer login 
pyautogui.press('tab')
pyautogui.write('leomarino1999@gmail.com')
pyautogui.press('tab')
pyautogui.write('sua senha definida')
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(5)

# 3- Abrir/Importar a base de produtos pra cadastrar
import pandas as pd
tabela = pd.read_csv("Projeto Automação/produtos.csv") 
print(tabela)

# 4- Cadastrar um produto
for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"]) 

    # clicar no campo de código
    pyautogui.click(x=653, y=294)

    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]

    # preencher o campo
    pyautogui.write(str(codigo))

    # passar para o proximo campo
    pyautogui.press("tab")

    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 

    # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

# 5- Repetir o processo de cadastro dos produtos até o final 