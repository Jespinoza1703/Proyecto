import pygame
import tkinter
from barra import Barra
from bola import Bola

BLACK = (0,0,0)
WHITE = (255,255,255)
L = 20

# Clase Juego:
# Atributos:
# matriz
#######################
# Metodos:
# crearMatriz()
# dibujarMatriz()
# jugar()
# colisionar()
ANCHO = 780
LARGO = 480

class Juego:
	def __init__(self):
		pygame.init()
		self.pantalla = pygame.display.set_mode((ANCHO,LARGO))
		pygame.display.set_caption("PONG")


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
		pygame.draw.line(self.pantalla, WHITE, [400, 0], [400,600], 4)