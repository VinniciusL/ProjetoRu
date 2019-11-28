from abc import ABC, abstractmethod
from tinydb import TinyDB, Query

class GenericDao(ABC):
	'''Classe que representa um DAO genérico'''
	def __init__(self):
		self._db = TinyDB('db.json')

	@abstractmethod
	def salvar(self, dado):
		'''Método abstrato para salvar'''
		pass

	@abstractmethod
	def atualizar(self,dado):
		'''Método abstrato para atualizar'''
		pass

	@abstractmethod
	def remover(self,dado):
		'''Método abstrato para remover'''

	@abstractmethod
	def listar(self,):
		'''Método abstrato para listar'''
		pass

	@property
	def db(self):
		return self._db
		