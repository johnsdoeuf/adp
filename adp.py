
class point():
	def __init__(self, x, y):
		self.x = float(x)
		self.y = float(y)
		self.poids = 1.0


	def fusion_xy(self, x ,y):
		self.x = (self.x * self.poids + x) / (poids + 1)
		self.y = (self.y * self.poids + y) / (poids + 1)