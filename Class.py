class Animal:


	def __init__(self, genero, tipo, patas, cor):

		self.genero = genero
		self.tipo = tipo
		self.patas = patas
		self.cor = cor


	def patasMudanca(self):
		if self.tipo == "Canino":
			self.patas = 4
			return self.patas
		else:
		 	return self.patas
			
			 

	def printAnimal(self):

		# "print(self.genero, self.tipo, patasMudanca(), self.cor)"
		return f"{self.genero} + {self.tipo} + {self.patasMudanca()} + {self.cor}"

		# return self.genero