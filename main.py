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