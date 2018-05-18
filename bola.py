# Clase Bola:
# Atributos:
# x
# y
# direction
# right
# vx
# vy
# socre1
# score2
#######################
# Metodos:
# mover_bola()
# get_score1()
# get_score2()
# set_score1()
# set_score2()
# get_x()
# get_y()

import random
import pygame
import os


class Bola:
	def __init__(self,x,y,direction,right):
		self.x = x
		self.y =y
		self.vx = 1
		self.vy = 1
		self.direction = direction
		self.right = right
		self.score1 = 0
		self.score2 = 0

	def get_score1(self):
		return self.score1

	def get_score2(self):
		return self.score2

	def set_score1(self, new_score):
		self.score1 = new_score

	def set_score2(self, new_score):
		self.score2 = new_score

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def mover(self, matriz):
		# se mueve primero en las filas y luego en las columnas
		matriz[self.y][self.x] = 0 #poner en negro el cuadro anterior

		if self.y == 24 and self.direction == -1: #cuando llegua abajo, cambie de direccion hacia arriba
			self.direction = 1
		elif self.y == 0 and self.direction == 1: #cuando llegue arriba, cambie de direccion hacia abajo
			self.direction = -1

		elif self.x == 37 and matriz[self.y][self.x + 1] == 0: #si llega al borde derecho y el cuadrado de matriz es negro, punto para jugador 1
			pygame.mixer.Sound(os.path.join('sounds', 'fail.wav')).play()
			self.right = False
			self.direction = random.randrange(-1, 2) #saque inicial direccion aleatorio
			self.score1 += 1
			self.x = 20
			self.y = 12

		elif self.x == 37 and matriz[self.y][self.x + 1] == 1: #si llega al final y el siguiente es blanco, rebote
			pygame.mixer.Sound(os.path.join('sounds', 'bounce.wav')).play()
			if matriz[self.y - 3][self.x + 1] == 0 and matriz[self.y + 3][self.x + 1] == 0: #revisa si paleta es de 3
				if matriz[self.y - 1][self.x + 1] == 0:
					self.direction = 1
					self.right = False
				elif matriz[self.y + 1][self.x + 1] == 0:
					self.direction = -1
					self.right = False
				else:
					self.direction = 0
					self.right = False
			if matriz[self.y - 3][self.x + 1] == 1 or matriz[self.y + 3][self.x + 1] == 1: #si paleta es 6
				if matriz[self.y - 2][self.x + 1] == 0:
					self.direction = 1
					self.right = False
				elif matriz[self.y + 2][self.x + 1] == 0:
					self.direction = -1
					self.right = False
				else:
					self.direction = 0
					self.right = False
			if matriz[self.y - 5][self.x + 1] == 1 or matriz[self.y + 5][self.x + 1] == 1: #si paleta es 9
				if matriz[self.y - 3][self.x + 1] == 0:
					self.direction = 1
					self.right = False
				elif matriz[self.y + 3][self.x + 1] == 0:
					self.direction = -1
					self.right = False
				else:
					self.direction = 0
					self.right = False

		elif self.x == 29 and matriz[self.y][self.x + 1] == 1: #si llega a la barra doble derecha y el siguiente es blanco, rebote
			pygame.mixer.Sound(os.path.join('sounds', 'bounce.wav')).play()
			if matriz[self.y - 3][self.x + 1] == 0 and matriz[self.y + 3][self.x + 1] == 0: #revisa si paleta es de 3
				if matriz[self.y - 1][self.x + 1] == 0:
					self.direction = 1
					self.right = False
				elif matriz[self.y + 1][self.x + 1] == 0:
					self.direction = -1
					self.right = False
				else:
					self.direction = 0
					self.right = False
			if matriz[self.y - 3][self.x + 1] == 1 or matriz[self.y + 3][self.x + 1] == 1: #si paleta es 6
				if matriz[self.y - 2][self.x + 1] == 0:
					self.direction = 1
					self.right = False
				elif matriz[self.y + 2][self.x + 1] == 0:
					self.direction = -1
					self.right = False
				else:
					self.direction = 0
					self.right = False
			if matriz[self.y - 5][self.x + 1] == 1 or matriz[self.y + 5][self.x + 1] == 1: #si paleta es 9
				if matriz[self.y - 3][self.x + 1] == 0:
					self.direction = 1
					self.right = False
				elif matriz[self.y + 3][self.x + 1] == 0:
					self.direction = -1
					self.right = False
				else:
					self.direction = 0
					self.right = False

		elif self.x == 2 and matriz[self.y][self.x -1] == 0: #si llega al principio y el siguiente cuadro es negro, rebote
			pygame.mixer.Sound(os.path.join('sounds', 'fail.wav')).play()
			self.right = True #si llega al borde izquierdo, cambie de direccion hacia derecha
			self.direction = random.randrange(-1, 2) #saque inicial direccion aleatoria
			self.score2 += 1
			self.x = 20
			self.y = 12

		elif self.x == 2 and matriz[self.y][self.x -1] == 1: #si llega al principio y el siguiente es blanco
			pygame.mixer.Sound(os.path.join('sounds', 'bounce.wav')).play()
			if matriz[self.y - 3][self.x - 1] == 0 and matriz[self.y + 3][self.x - 1] == 0: #revisa si paleta es de 3
				if matriz[self.y - 1][self.x - 1] == 0:
					self.direction = 1
					self.right = True
				elif matriz[self.y + 1][self.x - 1] == 0:
					self.direction = -1
					self.right = True
				else:
					self.direction = 0
					self.right = True
			if matriz[self.y - 3][self.x - 1] == 1 or matriz[self.y + 3][self.x - 1] == 1: #si paleta es 6
				if matriz[self.y - 2][self.x - 1] == 0:
					self.direction = 1
					self.right = True
				elif matriz[self.y + 2][self.x - 1] == 0:
					self.direction = -1
					self.right = True
				else:
					self.direction = 0
					self.right = True
			if matriz[self.y - 5][self.x - 1] == 1 or matriz[self.y + 5][self.x - 1] == 1: #si paleta es 9
				if matriz[self.y - 3][self.x - 1] == 0:
					self.direction = 1
					self.right = True
				elif matriz[self.y + 3][self.x - 1] == 0:
					self.direction = -1
					self.right = True
				else:
					self.direction = 0
					self.right = True

		elif self.x == 10 and matriz[self.y][self.x -1] == 1: #si llega a la paleta doble izquierda y el siguiente es blanco
			pygame.mixer.Sound(os.path.join('sounds', 'bounce.wav')).play()
			if matriz[self.y - 3][self.x - 1] == 0 and matriz[self.y + 3][self.x - 1] == 0: #revisa si paleta es de 3
				if matriz[self.y - 1][self.x - 1] == 0:
					self.direction = 1
					self.right = True
				elif matriz[self.y + 1][self.x - 1] == 0:
					self.direction = -1
					self.right = True
				else:
					self.direction = 0
					self.right = True
			if matriz[self.y - 3][self.x - 1] == 1 or matriz[self.y + 3][self.x - 1] == 1: #si paleta es 6
				if matriz[self.y - 2][self.x - 1] == 0:
					self.direction = 1
					self.right = True
				elif matriz[self.y + 2][self.x - 1] == 0:
					self.direction = -1
					self.right = True
				else:
					self.direction = 0
					self.right = True
			if matriz[self.y - 5][self.x - 1] == 1 or matriz[self.y + 5][self.x - 1] == 1: #si paleta es 9
				if matriz[self.y - 3][self.x - 1] == 0:
					self.direction = 1
					self.right = True
				elif matriz[self.y + 3][self.x - 1] == 0:
					self.direction = -1
					self.right = True
				else:
					self.direction = 0
					self.right = True

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
				print('score1: '+str(self.score1))
				print('score2: '+str(self.score2))
			elif self.direction == 1:
				self.x += self.vx
				self.y -= self.vy 
				print(2)
				print('direction: '+str(self.direction))
				print('right: '+str(self.right))
				print('x: '+str(self.x))
				print('y: '+str(self.y))
				print('score1: '+str(self.score1))
				print('score2: '+str(self.score2))
				matriz[self.y][self.x] = 1
			elif self.direction == 0:
				self.x += self.vx
				matriz[self.y][self.x] = 1
				print(3)
				print('direction: '+str(self.direction))
				print('right: '+str(self.right))
				print('x: '+str(self.x))
				print('y: '+str(self.y))
				print('score1: '+str(self.score1))
				print('score2: '+str(self.score2))

		elif self.right == False and self.x > 0: #si right es false, o sea hacia la izquierda
			if self.direction == -1:
				self.x -= self.vx
				self.y += self.vy
				matriz[self.y][self.x] = 1
				print(4)
				print('direction: '+str(self.direction))
				print('right: '+str(self.right))
				print('x: '+str(self.x))
				print('y: '+str(self.y))
				print('score1: '+str(self.score1))
				print('score2: '+str(self.score2))
			elif self.direction == 1:
				self.x -= self.vx
				self.y -= self.vy 
				print(5)
				print('direction: '+str(self.direction))
				print('right: '+str(self.right))
				print('x: '+str(self.x))
				print('y: '+str(self.y))
				print('score1: '+str(self.score1))
				print('score2: '+str(self.score2))
				matriz[self.y][self.x] = 1
			elif self.direction == 0:
				self.x -= self.vx
				matriz[self.y][self.x] = 1
				print(6)
				print('direction: '+str(self.direction))
				print('right: '+str(self.right))
				print('x: '+str(self.x))
				print('y: '+str(self.y))
				print('score1: '+str(self.score1))
				print('score2: '+str(self.score2))
