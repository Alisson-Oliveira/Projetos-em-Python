# coding:utf-8
from Usuarios import Usuarios
from tkinter import *

class Application:

    def __init__(self, master = None):
        self.fonte = ("Verdana", "10")
        self.fonteButton = ("Verdada", "10", "bold")

        # Containers

        # Container1
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        # Container2
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        
        # Container3
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        
        # Container4
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        
        # Container5
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        
        # Container6
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        
        # Container7
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        # Container8
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack() 
        
        # Container9
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()

        # Container10
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 10
        self.container10.pack()
        
        # Container11
        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 10
        self.container11.pack()
    
        # Container12
        self.container12 = Frame(master)
        self.container12["pady"] = 15
        self.container12.pack()
        
        # EVENTOS
        
        # Container 1
        self.titulo = Label(self.container1,
                            text = "Dados do Cliente")
        self.titulo["font"] = ("Calibri", "12", "bold")
        self.titulo.pack() 
        
        # Container 2
        self.lblidusuario = Label(  self.container2,
                                    text  = "ID Usuário:",
                                    font  = self.fonte,
                                    width = 10)
        self.lblidusuario.pack(side = LEFT)

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 8
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side = LEFT)
        
        self.btnBuscar = Button(self.container2,
                                text  = "Buscar",
                                font  = self.fonte,
                                width = 10)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side = RIGHT)
        
        # Container 3
        self.lblnome = Label(   self.container3,
                                text  = "Nome:",
                                font  = self.fonte,
                                width = 10)
        self.lblnome.pack(side = LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side = LEFT)

        #Container 4
        self.lblcpf = Label(self.container4,
                            text  = "CPF:",
                            font  = self.fonte,
                            width = 10)
        self.lblcpf.pack(side = LEFT)

        self.txtcpf = Entry(self.container4)
        self.txtcpf["width"] = 25
        self.txtcpf["font"] = self.fonte
        self.txtcpf.pack(side = LEFT)
        
        # Container 5
        self.lbltelefone = Label(   self.container5,
                                    text  = "Telefone:",
                                    font  = self.fonte,
                                    width = 10)
        self.lbltelefone.pack(side = LEFT)

        self.txttelefone = Entry(self.container5)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side = LEFT)
        
        # Container 6
        self.lblendereco = Label(   self.container6,
                                    text  = "Endereço:",
                                    font  = self.fonte,
                                    width = 10)
        self.lblendereco.pack(side = LEFT)

        self.txtendereco = Entry(self.container6)
        self.txtendereco["width"] = 25
        self.txtendereco["font"] = self.fonte
        self.txtendereco.pack(side=LEFT)
        
        # Container 7
        self.lblemail = Label(  self.container7, 
                                text  = "E-mail:",
                                font  = self.fonte,
                                width = 10)
        self.lblemail.pack(side = LEFT)

        self.txtemail = Entry(self.container7)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side = LEFT)
        
        # Container 8
        self.lblusuario = Label(self.container8,
                                text  = "Usuário:",
                                font  = self.fonte, 
                                width = 10)
        self.lblusuario.pack(side = LEFT) 
        
        self.txtusuario = Entry(self.container8)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side = LEFT)
        
        # Container 9
        self.lblsenha = Label(  self.container9,
                                text  = "Senha:",
                                font  = self.fonte,
                                width = 10)
        self.lblsenha.pack(side = LEFT)

        self.txtsenha = Entry(self.container9)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side = LEFT)

        # Botões (Inserir, Alterar, Excluir, Sair).
        
        # Container 8 
        
        # Botão Inserir
        self.bntInsert = Button(self.container10,
                                text  = "Inserir",
                                font  = self.fonteButton,
                                width = 12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack(side = LEFT)
        
        # Botão Alterar
        self.bntAlterar = Button(   self.container10,
                                    text  = "Alterar", 
                                    font  = self.fonteButton,
                                    width = 12)
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack(side = LEFT)
        
        # Botão Excluir
        self.bntExcluir = Button(   self.container10,
                                    text  = "Excluir",
                                    font  = self.fonteButton,
                                    width = 12)
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side = LEFT)

        # Container 9
        # Botão Sair
        self.bntSair = Button(  self.container11,
                                text  = "Sair",
                                font  = self.fonteButton, 
                                width = 12)
        self.bntSair["command"] = self.container1.quit
        self.bntSair.pack(side = LEFT)
        
        # Mensagem de ação, após execução.
        # Container 12
        # Mensagem
        self.lblmsg = Label(self.container12, text = "")
        self.lblmsg["font"] = ("Times New Roman", "9", "italic")
        self.lblmsg.pack()
    
    def inserirUsuario(self):
        user = Usuarios()

        user.nome = self.txtnome.get()
        user.cpf = self.txtcpf.get()
        user.telefone = self.txttelefone.get()
        user.endereco = self.txtendereco.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)
    
    def alterarUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get() 
        user.cpf = self.txtcpf.get()
        user.telefone = self.txttelefone.get()
        user.endereco = self.txtendereco.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
        
        self.lblmsg["text"] = user.updateUser()
        
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)
    
    def excluirUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.deleteUser()
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)
    
    def buscarUsuario(self):
        user = Usuarios()

        idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.selectUser(idusuario)

        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)

        self.txtcpf.delete(0, END)
        self.txtcpf.insert(INSERT, user.cpf)

        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT, user.telefone)

        self.txtendereco.delete(0, END)
        self.txtendereco.insert(INSERT, user.endereco)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)

        self.txtusuario.delete(0, END)
        self.txtusuario.insert(INSERT, user.usuario)

        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT, user.senha)

root = Tk()
root.title("Cadastro de Clientes")
Application(root)
root.mainloop()
