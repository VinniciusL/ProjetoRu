class Usuario:
    '''Classe que representa um usuario'''

    def __init__(self, id, login, senha, vinculo, ativo, pessoa):
        '''Método construtor da classe Usuario'''
        self._id = id
        self._login = login
        self._senha = senha
        self._vinculo = vinculo
        self._ativo = ativo
        self._pessoa = pessoa

    # Métodos getters e setters da classe Usuario

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        self._login = login

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def vinculo(self):
        return self._vinculo

    @vinculo.setter
    def vinculo(self, vinculo):
        self._vinculo = vinculo

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, ativo):
        self._ativo = ativo

    @property
    def pessoa(self):
        return self._pessoa

    @pessoa.setter
    def id(self, pessoa):
        self._pessoa = pessoa
