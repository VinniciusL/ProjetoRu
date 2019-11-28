# Definição do View  para a Pessoa
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar

# ================================ PARTE DE DEMONSTRAÇÃO DO USUARIO ======================================


class PessoaView:
    ''' Mostrar as informações da pessoa'''

    def __init__(self, master, controller):
        '''master=Janela Principal
           controller: define as ações
        '''
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Variaveis para os campos de texto
        self.vid = StringVar()
        self.vnome = StringVar()
        self.vcpf = StringVar()
        self.vemail = StringVar()

        # Criação dos rótulos e os campos de texto
        self.lid = tk.Label(self.frame, text="ID:")
        self.eid = tk.Entry(self.frame, textvariable=self.vid)
        self.lnome = tk.Label(self.frame, text="Nome:")
        self.enome = tk.Entry(self.frame, textvariable=self.vnome)
        self.lcpf = tk.Label(self.frame, text="CPF:")
        self.ecpf = tk.Entry(self.frame, textvariable=self.vcpf)
        self.lemail = tk.Label(self.frame, text="Email:")
        self.eemail = tk.Entry(self.frame, textvariable=self.vemail)
        self.btnAdd = tk.Button(self.frame, text="Adicionar")
        self.btnList = tk.Button(self.frame, text="Listar")
        self.btnClean = tk.Button(self.frame, text="Limpar")
        self.btnAvance = tk.Button(self.frame, text="Cartão")

        # Adicionar os widgets
        self.lid.grid(row=0, column=0)
        self.eid.grid(row=0, column=1)
        self.lcpf.grid(row=1, column=0)
        self.ecpf.grid(row=1, column=1)
        self.lnome.grid(row=2, column=0)
        self.enome.grid(row=2, column=1)
        self.lemail.grid(row=3, column=0)
        self.eemail.grid(row=3, column=1)
        self.btnAdd.grid(row=4, column=0)
        self.btnList.grid(row=4, column=1)
        self.btnClean.grid(row=4, column=2)
        self.btnAvance.grid(row=6, column=0)

        # Ações para os botões
        # Note que a ação do botão chama um método do controlador
        self.btnAdd.bind("<Button>", lambda e: controller.cadastrar_pessoa(self.vid.get(), self.vnome.get(), self.vcpf.get(), self.vemail.get()))

        self.btnList.bind("<Button>", lambda e: controller.listar_pessoas())

        # A ação deste botão chama direitamente um dos métodos do view
        self.btnClean.bind("<Button>", lambda e: self.limpar())

        # A ação deste botão é para ir diretamente a parte dos cartões
        self.btnAvance.bind("<Button>", lambda e: self.CartaoView())

        # Focus no CPF
        self.ecpf.focus_set()

    def limpar(self):
        '''Remover os textos dos campos'''
        self.vid.set("")
        self.vnome.set("")
        self.vcpf.set("")
        self.vemail.set("")
        # Focus no campo CPF
        self.ecpf.focus_set()

    def adicionar_ok(self):
        '''Mostrar uma mensagem informando que a operação foi bem sucedida'''
        messagebox.showinfo("Pessoa", "Pessoa Adicionada (CPF = {0})!".format(self.vcpf.get()))

    def adicionar_erro(self):
        ''' Mostrar uma mensagem de erro'''
        messagebox.showerror("Pessoa", "Impossível adicionar duas pessoas com o mesmo CPF = {0}".format(self.vcpf.get()))

    def mostrar_pessoa(self, p, win):
        '''
        Mostrar as informações da pessoa
        Note que esta função retorna outra função (necessária para
        implementar o command do botão)
        '''
        def fmostrar(e):
            self.vid.set(p.id)
            self.vnome.set(p.nome)
            self.vcpf.set(p.cpf)
            self.vemail.set(p.email)
            # Fechar a janela
            win.destroy()
            self.ecpf.focus_set()
        return fmostrar

    def listar(self, L):
        '''Mostrar a lista de pessoas L'''
        win = tk.Toplevel()
        win.wm_title("Lista de Pessoas")

        tk.Label(win, text="ID", bg="black", fg="white",
                 width=5).grid(row=0, column=0)
        tk.Label(win, text="CPF", bg="black", fg="white",
                 width=15).grid(row=0, column=1)
        tk.Label(win, text="Nome", bg="black", fg="white",
                 width=40).grid(row=0, column=2)
        tk.Label(win, text="Email", bg="black", fg="white",
                 width=20).grid(row=0, column=3)
        i = 1
        for p in L:
            LCPF = tk.Label(win, text=p.cpf, fg="blue")
            LCPF.bind("<Button>", self.mostrar_pessoa(p, win))
            LCPF.grid(row=i, column=0)
            tk.Label(win, text=p.nome).grid(row=i, column=1)
            tk.Label(win, text=p.email).grid(row=i, column=2)
            i += 1

# ================================ PARTE DE DEMONSTRAÇÃO DO CARTÃO ======================================


class CartaoView:
    ''' Mostrar as informações da pessoa'''

    def __init__(self, master, controller):

        # Configuração da janela principal
        '''master=Janela Principal controller: define as ações'''
        self.controller = controller
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Variaveis para os campos de texto
        self.vid = StringVar()
        self.vcodigo = StringVar()
        self.vsaldo = StringVar()
        self.vusuario = StringVar()

        # Criação dos rótulos e os campos de texto
        self.lid = tk.Label(self.frame, text="ID:")
        self.eid = tk.Entry(self.frame, textvariable=self.vid)
        self.lcodigo = tk.Label(self.frame, text="Código:")
        self.ecodigo = tk.Entry(self.frame, textvariable=self.vcodigo)
        self.lsaldo = tk.Label(self.frame, text="Saldo:")
        self.esaldo = tk.Entry(self.frame, textvariable=self.vsaldo)
        self.lusuario = tk.Label(self.frame, text="Usuario:")
        self.eusuario = tk.Entry(self.frame, textvariable=self.vusuario)
        self.btnAdd = tk.Button(self.frame, text="Adicionar")
        self.btnList = tk.Button(self.frame, text="Listar")
        self.btnClean = tk.Button(self.frame, text="Limpar")

        # Adicionar os widgets
        self.lid.grid(row=0, column=0)
        self.eid.grid(row=0, column=1)
        self.lcodigo.grid(row=1, column=0)
        self.ecodigo.grid(row=1, column=1)
        self.lsaldo.grid(row=2, column=0)
        self.esaldo.grid(row=2, column=1)
        self.lusuario.grid(row=3, column=0)
        self.eusuario.grid(row=3, column=1)
        self.btnAdd.grid(row=4, column=0)
        self.btnList.grid(row=4, column=1)
        self.btnClean.grid(row=4, column=2)

        # Ações para os botões
        # Note que a ação do botão chama um método do controlador
        self.btnAdd.bind("<Button>", lambda e: controller.cadastrar_cartao(
            self.vid.get(), self.vcodigo.get(), self.vsaldo.get(), self.vusuario.get()))

        self.btnList.bind("<Button>", lambda e: controller.listar_cartao())

        # A ação deste botão chama direitamente um dos métodos do view
        self.btnClean.bind("<Button>", lambda e: self.limpar())

        # Focus no Codigo
        self.ecodigo.focus_set()

    def limpar(self):
        '''Remover os textos dos campos'''
        self.vid.set("")
        self.vcodigo.set("")
        self.vsaldo.set("")
        self.vusuario.set("")
        # Focus no campo CPF
        self.esaldo.focus_set()

    def adicionar_ok(self):
        '''Mostrar uma mensagem informando que a operação foi bem sucedida'''
        messagebox.showinfo(
            "Cartão", "Cartão Adicionado (Cartão = {0})!".format(self.vcodigo.get()))

    def adicionar_erro(self):
        ''' Mostrar uma mensagem de erro'''
        messagebox.showerror(
            "Cartao", "Impossível adicionar dois cartões com o mesmo codigo = {0}".format(self.vcodigo.get()))

    def mostrar_cartao(self, p, win):
        '''
        Mostrar as informações da pessoa
        Note que esta função retorna outra função (necessária para
        implementar o command do botão)
        '''
        def fmostrar(e):
            self.vid.set(p.id)
            self.vcodigo.set(p.codigo)
            self.vsaldo.set(p.saldo)
            self.vusuario.set(p.usuario)
            # Fechar a janela
            win.destroy()
            self.ecodigo.focus_set()
        return fmostrar

    def listar(self, C):
        '''Mostrar a lista de Cartões C'''
        win = tk.Toplevel()
        win.wm_title("Lista de Cartões")

        tk.Label(win, text="ID", bg="black", fg="white",
                 width=5).grid(row=0, column=0)
        tk.Label(win, text="Saldo", bg="black", fg="white",
                 width=15).grid(row=0, column=1)
        tk.Label(win, text="Código", bg="black", fg="white",
                 width=40).grid(row=0, column=2)
        tk.Label(win, text="Usuário", bg="black", fg="white",
                 width=20).grid(row=0, column=3)
        i = 1
        for p in C:
            LCPF = tk.Label(win, text=p.codigo, fg="blue")
            LCPF.bind("<Button>", self.mostrar_cartao(p, win))
            LCPF.grid(row=i, column=0)
            tk.Label(win, text=p.usuario).grid(row=i, column=1)
            tk.Label(win, text=p.saldo).grid(row=i, column=2)
            i += 1
