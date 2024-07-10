import pyautogui
import time
from Importacao import Tarefas 
from Produto import Produto 

# comando "pyautogui.PAUSE" = tempo de execução/intervalo de um comando para o outro
pyautogui.PAUSE = 2 

# Criando a classe "Navegador"
class Navegador:
    def __init__(self):
        pass 

# metodo 1 = abrir navegador google chorme    
    def abrir_navegador(self): 
        pyautogui.press('win')
        pyautogui.write('chrome')
        pyautogui.press('enter') 
        
# metodo 2 = entrar no sistema 
    def entrar_sistema(self):
        pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
        pyautogui.press('enter') 
# comando "time.sleep(x=tempo)" = tempo de carregamento do comando executado
        time.sleep(3) 

# metodo 3 = fazer login
    def fazer_login(self, email, senha):
        pyautogui.press('tab')
        pyautogui.write(email)
        pyautogui.press('tab')
        pyautogui.write(senha)
        pyautogui.press('enter')
        time.sleep(3) 

# metodo 4 = cadastro produto
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