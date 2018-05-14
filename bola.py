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

import random

class Bola:
	def __init__(self,x,y, direction, right):
		self.x = x
		self.y =y
		self.vx = 1
		self.vy = 1
		self.direction = direction
		self.right = True

	def mover(self, matriz):
		# se mueve primero en las filas y luego en las columnas
		matriz[self.y][self.x] = 0


		if self.y == 23 and self.direction == -1: #cuando llegua abajo, cambie de direccion hacia arriba
			self.direction = 1
		elif self.y == 1 and self.direction == 1: #cuando llegue arriba, cambie de direccion hacia abajo
			self.direction = -1

		elif self.x == 38:
			self.right = False
		elif self.right == False and self.x < 39:
			self.right = False
		elif self.right == True and self.x < 39:
			self.right = True

		if self.right == True: #si right es true, o sea, hacia la derecha
			if self.x < 38 and self.direction == -1:
				print(1)
				self.x += self.vx
				self.y += self.vy
				matriz[self.y][self.x] = 1
				print('direction: '+str(self.direction))
				print('right: '+str(self.right))
				print('x: '+str(self.x))
				print('y: '+str(self.y))
				#elif self.x == 24 or self.y < 39:
					#print(3)
					#self.x += self.vx
					#self.y += self.vy
					#matriz[self.y][self.x] = 1
			elif self.x < 38 and self.direction == 1:
				print(2)
				self.x += self.vx
				self.y -= self.vy 
				print('direction: '+str(self.direction))
				print('right: '+str(self.right))
				print('x: '+str(self.x))
				print('y: '+str(self.y))
				matriz[self.y][self.x] = 1
			elif self.x < 38 and self.direction == 0:
				print(3)
				self.x += self.vx
				print('direction: '+str(self.direction))
				print('right: '+str(self.right))
				print('x: '+str(self.x))
				print('y: '+str(self.y))
				matriz[self.y][self.x] = 1

		elif self.right == False: #si right es false, o sea hacia la izquierda
			print(0, self.x, self.y, self.direction)
			if self.x != 39 and self.y != 24 and self.direction == True:
				print(4)
				self.x -= self.vx
				self.y += self.vy
				matriz[self.y][self.x] = 1
				print(self.direction)
				print('x: '+str(self.x))
				print('y: '+str(self.y))
			elif self.x != 39 and self.y != 1 and self.direction == False:
				print(5)
				self.x -= self.vx
				self.y -= self.vy 
				print('x: '+str(self.x))
				print('y: '+str(self.y))
				matriz[self.y][self.x] = 1