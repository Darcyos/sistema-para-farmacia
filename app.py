from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import tkinter.messagebox as MessageBox
import re
import mysql.connector

conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= '',
    database= 'point_farma'
)
cursor = conexao.cursor()

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
        comando = "SELECT * FROM cliente where email = %s and senha = %s"
        valores = (usuario, senha)
        cursor.execute(comando, valores)
        
        if cursor.fetchone() is not None:
            self.successful_login()
        else:
            print("Falha na autenticação. Usuário ou senha inválidos.")


         
    


    def successful_login(self):
        self.manager.current = 'logado'

class App(MDApp):
    def build(self):
        self.title='point farma'
        return Builder.load_file('tela.kv')
    
    
    

App().run()
cursor.close()
conexao.close()




 #identificar se os dados inseridos é de um email 
'''if re.match(r"[^@]+@[^@]+\.[^@]+", usuario):
            tipo = 'email'
    
        if tipo=='email':
            comando = f"SELECT * FROM cliente where email = '{usuario}'"
            cursor.execute(comando)
            dados = cursor.fetchall() 

                #self.successful_login()

            #identificar se os dados inseridos é de um celular
        elif re.match(r"\d{2}\s?\d{4,5}\s?\d{4}", usuario):
            comandouser = f"SELECT numero FROM cliente where numero = '{usuario}'"
            cursor.execute(comandouser)
            user = cursor.fetchall()
            comandosenha = f"SELECT senha FROM cliente where email = '{usuario}'"
            cursor.execute(comandosenha)
            password = cursor.fetchall()'''