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
		matriz[self.y][self.x] = 0 #poner en negro el cuadro anterior


		if self.y == 24 and self.direction == -1: #cuando llegua abajo, cambie de direccion hacia arriba
			self.direction = 1
		elif self.y == 1 and self.direction == 1: #cuando llegue arriba, cambie de direccion hacia abajo
			self.direction = -1

		elif self.x == 39: #si llega al borde derecho, cambie de direccion hacia izquierda
			self.right = False
		elif self.x == 1:
			self.right = True #si llega al borde izquierdi, cambie de direccion hacia derecha

		if self.right == True: #si right es true, o sea, hacia la derecha
			if self.direction == -1:
				self.x += self.vx
				self.y += self.vy
				matriz[self.y][self.x] = 1
				print(1)
				print('direction: '+str(self.direction))
				print('right: '+str(self.right))
				print('x: '+str(self.x))
				print('y: '+str(self.y))
			elif self.direction == 1:
				self.x += self.vx
				self.y -= self.vy 
				print(2)
				print('direction: '+str(self.direction))
				print('right: '+str(self.right))
				print('x: '+str(self.x))
				print('y: '+str(self.y))
				matriz[self.y][self.x] = 1
			elif self.direction == 0:
				self.x += self.vx
				matriz[self.y][self.x] = 1
				print(3)
				print('direction: '+str(self.direction))
				print('right: '+str(self.right))
				print('x: '+str(self.x))
				print('y: '+str(self.y))

		if self.right == False: #si right es false, o sea hacia la izquierda
			if self.direction == -1:
				self.x -= self.vx
				self.y += self.vy
				matriz[self.y][self.x] = 1
				print(4)
				print('direction: '+str(self.direction))
				print('right: '+str(self.right))
				print('x: '+str(self.x))
				print('y: '+str(self.y))
			elif self.direction == 1 and self.x > 0:
				self.x -= self.vx
				self.y -= self.vy 
				print(5)
				print('direction: '+str(self.direction))
				print('right: '+str(self.right))
				print('x: '+str(self.x))
				print('y: '+str(self.y))
				matriz[self.y][self.x] = 1
			elif self.direction == 0:
				self.x -= self.vx
				matriz[self.y][self.x] = 1
				print(6)
				print('direction: '+str(self.direction))
				print('right: '+str(self.right))
				print('x: '+str(self.x))
				print('y: '+str(self.y))