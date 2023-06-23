from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import tkinter.messagebox as MessageBox

import mysql.connector

'''conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '',
    database= 'escola_ete'
)
cursor = conexao.cursor()'''

class GerenciarLogin(ScreenManager):
    pass

class GerenciarLogado(Screen):
    pass

class JanelaPrincipal(Screen):
    pass

class CadastroEmail(Screen):
    def adicionar(self):
        nome = self.ids.nome.text
        email = self.ids.email.text
        cpf = self.ids.cpf.text
        endereço = self.ids.endereço.text
        senha = self.ids.senha.text
        print(f'nome{nome},email{email},cpf{cpf},enderço{endereço},senha{senha}')
        MessageBox.showinfo("Sucesso!", "Cadastro realizado com sucesso!")
        

class CadastroTelefone(Screen):
    def adicionar(self):
        nome = self.ids.nome.text
        telefone = self.ids.telefone.text
        cpf = self.ids.cpf.text
        endereço = self.ids.endereço.text
        senha = self.ids.senha.text
        print(f'nome{nome},telefone{telefone},cpf{cpf},enderço{endereço},senha{senha}')
        MessageBox.showinfo("Sucesso!", "Cadastro realizado com sucesso!")
            
class Login(Screen):
    def entrar(self):
        usuario = self.ids.usuario.text
        senha = self.ids.senha.text
        if usuario =='darcyo' and senha=="123456":
            return GerenciarLogado
        else:
            MessageBox.showinfo("ERRO!", "usuario ou senha invalidos!")



class App(MDApp):
    def build(self):
        self.title='point farma'
        return Builder.load_file('tela.kv')
    
    
    

App().run()
'''cursor.close()
conexao.close()'''