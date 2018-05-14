# Clase Barra:
# Atributos:
# x
# y
# ancho
# largo
# vel_y
#######################
# Metodos:
# mover_barra()

class Barra:
	def __init__(self,x,y,largo):
		self.ancho = 1
		self.largo = largo
		self.x = x
		self.y = y
		self.up = False
		self.vy = 1

	def posicionar(self,matriz):
		for n in range(self.largo):
			matriz[self.y+n][self.x] = 1

	def mover(self,matriz,direccion):
		matriz[self.y][self.x] = 0
		if self.y == 24: #si llega al borde derecho, cambie de direccion hacia izquierda
			self.up = False
		elif self.y == 0:
			self.up = True #si llega al borde izquierdi, cambie de direccion hacia derecha

		if self.up == True: #si up es true, o sea, hacia la derecha
			if self.direccion == -1:
				self.y += self.vy
				matriz[self.y][self.x] = 1
			elif self.direccion == 1:
				self.y -= self.vy 
				matriz[self.y][self.x] = 1
