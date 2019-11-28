class Pessoa:
	'''Classe que representa uma pessoa'''

	def __init__(self, idU, nome, cpf, email):
		'''Método construtor da classe pessoa'''
		self._id = id
		self._nome = nome
		self._cpf = cpf
		self._email = email

	# Métodos getters e setters da classe pessoa

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, nome):
		self._nome = nome

	@property
	def cpf(self):
		return self._cpf

	@cpf.setter
	def cpf(self, cpf):
		self._cpf = cpf

	@property
	def email(self):
		return self._email

	@email.setter
	def email(self, email):
		self._email = email

class CPFRepetido (Exception):
    '''
    Exceção lançada ao tentar cadastrar duas pessoas com o 
    mesmo CPF
    '''
    def __init__(self):
        super().__init__("CPF Repetido")
