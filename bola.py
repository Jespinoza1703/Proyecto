# Clase Bola:
# Atributos:
# x
# y
# ancho
# largo
# vy
# vx
#######################
# Metodos:
# mover_bola()

class Bola:
	def __init__(self,x,y):
		self.x = x
		self.y =y
		self.vx = 1
		self.vy = 1

	def mover(self, matriz):
		# se mueve primero en las filas y luego en las columnas
		matriz[self.y][self.x] = 0
		self.x += self.vx
		self.y += self.vy
		matriz[self.y][self.x] = 1
