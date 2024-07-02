# Transformando o codigo em função

from Navegador import Navegador
from Usuario import Usuario
import pyautogui
import time

def abrir_navegador():
    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press('enter') 

abrir_navegador() 

def entrar_sistema():
    pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
    pyautogui.press('enter') 
    time.sleep(5)

entrar_sistema()

def login_usuario():
    pyautogui.press('tab')
    pyautogui.write('leomarino1999@gmail.com') 

login_usuario()

def senha_usuario():
    pyautogui.press('tab')
    pyautogui.write('sua senha definida')
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(5) 

senha_usuario() 