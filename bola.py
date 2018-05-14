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
		self.down = None

	def mover(self, matriz):
		# se mueve primero en las filas y luego en las columnas
		if self.y == 23:
			self.down = False
		elif self.down == False and self.x > 1:
			self.down = False
		elif self.down == None and self.x > 1:
			self.down = True
		matriz[self.y][self.x] = 0
		if self.x != 39 and self.y != 24 and self.down == True:
			if self.x < 39 and self.y < 23:
				print(1)
				self.x += self.vx
				self.y += self.vy
				matriz[self.y][self.x] = 1
				print(self.down)
				print('x: '+str(self.x))
				print('y: '+str(self.y))
			elif self.y == 23:
				matriz[self.y][self.x] = 1
				down = False
				print(self.down)
				print('hello')
				self.mover(matriz, self.down)
			#elif self.x == 24 or self.y < 39:
				#print(3)
				#self.x += self.vx
				#self.y += self.vy
				#matriz[self.y][self.x] = 1
		elif self.x != 39 and self.y != 1 and self.down == False:
			if self.x != 39 or self.y != 24:
				print(2)
				self.x += self.vx
				self.y -= self.vy 
				matriz[self.y][self.x] = 1