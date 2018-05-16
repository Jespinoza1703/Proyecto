# Clase Barra:
# Atributos:
# x1
# y1
# x2
# y2
# ancho
# largo
# vel_y
####################### 
# Metodos:
# mover_barra()

class Barra_doble:
	def __init__(self,x1,y1,x2,y2,largo):
		self.ancho = 1
		self.largo = largo
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

	def get_y1(self):
		return self.y1

	def get_y2(self):
		return self.y2

	# Coloca la barra en la matriz
	def posicionar(self,matriz):
		for n in range(self.largo):
			matriz[self.y1+n][self.x1] = 1
		for n in range(self.largo):
			matriz[self.y2+n][self.x2] = 1
	# Permite mover la barra sin que mueva a través de la matriz
	def mover(self,vy,matriz):
		if vy == -1 and self.y1 + self.largo < 25 and self.y2 - self.largo < 25:
			matriz[self.y1][self.x1] = 0
			matriz[self.y2][self.x2] = 0
			self.y1 -= vy
			self.y2 -= vy
			matriz[self.y1][self.x1] = 1
			matriz[self.y2][self.x2] = 1
		elif vy == 1 and self.y1 > 0 and self.y2 > 0:
			matriz[self.y1 + self.largo - 1][self.x1] = 0
			matriz[self.y2 + self.largo - 1][self.x2] = 0
			self.y1 -= vy
			self.y2 -= vy
			matriz[self.y1][self.x1] = 1
			matriz[self.y2][self.x2] = 1
