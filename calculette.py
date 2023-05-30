class Error(Exception):
	pass

class Calculette:

	def __init__(self):
		self.res = 0

	def add(self,a,b):
		self.res = a + b
		print(self.res)

	def divide(self,a, b):
		if b < 1:
			raise Error("vous êtes sûr????")
		self.res =  a / b
		print(self.res)

	def test(self):
		self.res = 0

if __name__ == '__main__':
	c = Calculette()
	c.add(1,2)
	c.divide(1,2)
	c.divide(1,"toto")
	c.divide('a',1)