class Porcao:
	'''Classe que representa uma porção de comida'''

	def __init__(self, id, denominacao):
		'''Método construtor da classe Porcao'''
		self._id = id
		self._denominacao = denominacao

	#Métodos getters e setters da classe Porcao

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
	def denominacao(self, denominacao):
		self._denominacao = denominacao