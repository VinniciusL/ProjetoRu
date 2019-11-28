class Refeicao:
    '''Classe que representa uma refeição'''

    def __init__(self, denominacao):
        '''Método construtor da classe Refeicao'''
        self._id = id
        self._denominacao = denominacao
        self._porcoes = []

    # Métodos getters e setters da classe Refeicao

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def denominacao(self):
        return self._denominacao

    @denominacao.setter
    def id(self, denominacao):
        self._denominacao = denominacao

    @property
    def porcoes(self):
        return self._porcoes

    @porcoes.setter
    def porcoes(self, porcoes):
        self._porcoes = porcoes
