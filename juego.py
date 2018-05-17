import pygame
import tkinter
from barra import Barra
from bola import Bola
from barra_doble import Barra_doble
import time
import random
import os

BLACK = (0,0,0)
WHITE = (255,255,255)
L = 20

# Clase Juego:
# Atributos:
# matriz: [[],[],...,[]]
# bola: Class
# barra1: Class
# barra2: Class
# score: int
#######################
# Metodos:
# crearMatriz()
# dibujarMatriz()
# jugar()
# colisionar()
ANCHO = 800
LARGO = 500

TIEMPO_NIVEL1 = 0.1
TIEMPO_NIVEL2 = 0.07
TIEMPO_NIVEL3 = 0.04

TAMAÑO_BARRA_1 = 9
TAMAÑO_BARRA_2 = 6
TAMAÑO_BARRA_3 = 3

class Juego:
	def __init__(self, modo, nivel, versus):
		pygame.init()
		self.pantalla = pygame.display.set_mode((ANCHO,LARGO))
		pygame.display.set_caption("Pong")
		self.FILAS = 30
		self.COLUMNAS = 40
		self.matriz = []
		self.crearMatriz()
		self.score = 0
		self.bola = Bola(20,12, random.randrange(-1, 2), True)
		self.nivel = nivel
		self.modo = modo
		self.versus = versus
		self.CPU = 0
		if self.nivel == 1:
			self.tiempo = TIEMPO_NIVEL1
			if self.modo == "Single":
				self.barra1 = Barra(1,2,TAMAÑO_BARRA_1) 
				self.barra2 = Barra(38,2,TAMAÑO_BARRA_1)
				if self.versus == "humano":
					self.CPU = 0
				elif self.versus == "cpu":
					self.CPU = 1

			else:
				self.barra1 = Barra_doble(1,3,9,13,TAMAÑO_BARRA_1)
				self.barra2 = Barra_doble(38,12,30,3,TAMAÑO_BARRA_1)
				if self.versus == "humano":
					self.CPU = 0
				elif self.versus == "cpu":
					self.CPU = 1
		elif self.nivel == 2:
			self.tiempo = TIEMPO_NIVEL2
			if self.modo == "Single":
				self.barra1 = Barra(1,2,TAMAÑO_BARRA_2) 
				self.barra2 = Barra(38,2,TAMAÑO_BARRA_2)
				if self.versus == "humano":
					self.CPU = 0
				elif self.versus == "cpu":
					self.CPU = 1
			else:
				self.barra1 = Barra_doble(1,3,9,13,TAMAÑO_BARRA_2)
				self.barra2 = Barra_doble(38,12,30,3,TAMAÑO_BARRA_2)
				if self.versus == "humano":
					self.CPU = 0
				elif self.versus == "cpu":
					self.CPU = 1
		elif self.nivel == 3:
			self.tiempo = TIEMPO_NIVEL3
			if self.modo == "Single":
				self.barra1 = Barra(1,2,TAMAÑO_BARRA_3) 
				self.barra2 = Barra(38,2,TAMAÑO_BARRA_3)
				if self.versus == "humano":
					self.CPU = 0
				elif self.versus == "cpu":
					self.CPU = 1
			else:
				self.barra1 = Barra_doble(1,3,9,13,TAMAÑO_BARRA_3)
				self.barra2 = Barra_doble(38,12,30,3,TAMAÑO_BARRA_3)
				if self.versus == "humano":
					self.CPU = 0
				elif self.versus == "cpu":
					self.CPU = 1

	def crearMatriz(self):
		for i in range(self.FILAS):
			fila = []
			for j in range(self.COLUMNAS):
				# Llena la lista de ceros
				fila.append(0)
			self.matriz.append(fila)

	def dibujarMatriz(self):
		for fila in range(self.FILAS):
			for columna in range(self.COLUMNAS):
				if self.matriz[fila][columna] == 0:
					pygame.draw.rect(self.pantalla, BLACK, [L* columna,L * fila,L,L])
				else:
					pygame.draw.rect(self.pantalla, WHITE, [L* columna,L * fila,L,L])
		time.sleep(self.tiempo)
		pygame.draw.line(self.pantalla, WHITE, [ANCHO//2, 0], [ANCHO//2,LARGO], 4)

	def cpu(self):
		if self.bola.get_x() > 28:
			if self.bola.get_y() > self.barra2.get_y():
				self.barra2.mover(-1, self.matriz)
			else:
				self.barra2.mover(1, self.matriz)

	def jugar(self):
		# Pone la bola en la matriz
		fuera_juego = False
		while not fuera_juego:
			if self.bola.get_score1() == 5 or self.bola.get_score2() == 5:
				self.bola.set_score1(0)
				self.bola.set_score2(0)
				self.nivel += 1

				self.matriz = []
				self.crearMatriz()

				if self.nivel == 1:
					self.tiempo = TIEMPO_NIVEL1
					if self.modo == "Single":
						self.barra1 = Barra(1,2,TAMAÑO_BARRA_1) 
						self.barra2 = Barra(38,2,TAMAÑO_BARRA_1)
					else:
						self.barra1 = Barra_doble(1,3,9,13,TAMAÑO_BARRA_1)
						self.barra2 = Barra_doble(38,12,30,3,TAMAÑO_BARRA_1)
				if self.nivel == 2:
					self.tiempo = TIEMPO_NIVEL2
					if self.modo == "Single":
						self.barra1 = Barra(1,2,TAMAÑO_BARRA_2) 
						self.barra2 = Barra(38,2,TAMAÑO_BARRA_2)
					else:
						self.barra1 = Barra_doble(1,3,9,13,TAMAÑO_BARRA_2)
						self.barra2 = Barra_doble(38,12,30,3,TAMAÑO_BARRA_2)

				if self.nivel == 3:
					self.tiempo = TIEMPO_NIVEL3
					if self.modo == "Single":
						self.barra1 = Barra(1,2,TAMAÑO_BARRA_3) 
						self.barra2 = Barra(38,2,TAMAÑO_BARRA_3)
					else:
						self.barra1 = Barra_doble(1,3,9,13,TAMAÑO_BARRA_3)
						self.barra2 = Barra_doble(38,12,30,3,TAMAÑO_BARRA_3)

				if self.nivel == 3:
					self.nivel = 0

		
			for event in pygame.event.get():
				if event.type == pygame.QUIT: #is le da X, cierra todo
					pygame.quit()
					quit()
				if event.type == pygame.KEYDOWN: #al presionar una tecla
					if event.key == pygame.K_UP:
						self.barra2.mover(1,self.matriz)
					elif event.key == pygame.K_DOWN:
						self.barra2.mover(-1,self.matriz)
					elif event.key == pygame.K_w:
						self.barra1.mover(1,self.matriz)
					elif event.key == pygame.K_s:
						self.barra1.mover(-1,self.matriz)
					elif event.key == pygame.K_ESCAPE:
						pygame.quit()
						quit()

			self.dibujarMatriz()

			self.dibujar()

			if self.CPU == 1:
				self.cpu()

			
	def dibujar(self):
		font = pygame.font.Font(None, 100)
		score1 = self.bola.get_score1()
		score_text = font.render(str(score1), True,
								 (WHITE))
		self.pantalla.blit(score_text, (150, 0))
		score2 = self.bola.get_score2()
		score_text2 = font.render(str(score2), True,
								 (WHITE))
		self.pantalla.blit(score_text2, (620, 0))
		# Pone la bola en la matriz
		self.bola.mover(self.matriz)
		self.barra1.posicionar(self.matriz)
		self.barra2.posicionar(self.matriz)
		pygame.display.update()
