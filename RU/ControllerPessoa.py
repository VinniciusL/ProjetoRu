#Classe do controlador

import tkinter as tk
from RUView import PessoaView
# from genericDao import GenericDao
from pessoa import Pessoa
from pessoa import CPFRepetido


class Controller:
    '''
    O controlador define 2 ações:
     - adicionar_pessoa: para adicionar novas pessoas no banco de
       dados.  
     - listar_pessoas: retornar a lista das pessoas

     Note que as 2 ações supracitadas utilizam a classe do Modelo para
     consultar/atualizar o banco de dados
    '''

    def __init__(self):
        # Criar a Janela principal
        self.root = tk.Tk()
        self.root.geometry('400x200+100+100')
        self.root.title('Pessoa')

        # Criar o objeto View
        self.view = PessoaView(self.root, self)

        #Loop
        self.root.mainloop()

    def cadastrar_pessoa(self, id, nome, cpf, email):
        '''
        Adicionar uma pessoa. Note que depois de utilizar os métodos
        do Modelo, um método apropriado do View é utilizado
        '''
        P = Pessoa(id, cpf, nome, email)
        try:
            Pessoa.cadastrar(P)
            self.view.cadastrar_ok()
        except CPFRepetido:
            self.view.cadastrar_erro()
            
    def listar_pessoas(self):
        self.view.listar(Pessoa.listar())