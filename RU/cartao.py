class Cartao:
	'''Classe que representa um cartão'''

	def __init__(self, id, codigo, saldo, usuario):
		'''Método construtor da classe Cartao'''
		self._id = id
		self._codigo = codigo
		self._saldo = saldo
		self._usuario = usuario

	#Métodos getters e setters da classe Cartao

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def codigo(self):
		return self._codigo

	@codigo.setter
	def codigo(self, codigo):
		self._codigo = codigo

	@property
	def saldo(self):
		return self._saldo

	@saldo.setter
	def saldo(self, saldo):
		self._saldo = saldo

	@property
	def usuario(self):
		return self._usuario

	@usuario.setter
	def usuario(self, usuario):
		self._usuario = usuario