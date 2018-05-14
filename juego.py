import pygame
import tkinter
from barra import Barra
from bola import Bola
import time

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
ANCHO = 780
LARGO = 480

class Juego:
	def __init__(self):
		pygame.init()
		self.pantalla = pygame.display.set_mode((ANCHO,LARGO))
		pygame.display.set_caption("PONG")
		self.FILAS = 25
		self.COLUMNAS = 40
		self.matriz = []
		self.crearMatriz()
		self.bola = Bola(5,5)
		self.barra1 = Barra(1,5,1,9)
		self.barra2 = Barra(38,5,1,9)
		self.score = 0


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
		time.sleep(0.08)
		pygame.draw.line(self.pantalla, WHITE, [400, 0], [400,600], 4)

	def jugar(self):
		# Pone la bola en la matriz
		self.bola.mover(self.matriz)
		fuera_juego = False
		while not fuera_juego:
			for event in pygame.event.get():
				if event.type == pygame.QUIT: #is le da X, cierra todd
					fuera_juego = True
				if event.type == pygame.KEYDOWN: #al presionar una tecla
					if event.key == pygame.K_UP:
						movimiento = -1
						barra.mover(movimiento,38)
						barra.actualiza_matriz(self.pantalla)
					elif event.key == pygame.K_DOWN:
						movimiento = 1
						barra.mover(movimiento,38)
						barra.actualiza_matriz(self.pantalla)
					elif event.key == pygame.K_w:
						movimiento = -1
						barra.mover2(movimiento,1)
						barra.actualiza_matriz(self.pantalla)
					elif event.key == pygame.K_s:
						movimiento = 1
						barra.mover2(movimiento,1)
						barra.actualiza_matriz(self.pantalla)
			self.dibujarMatriz()
			self.dibujar()

			
	def dibujar(self):
		font = pygame.font.Font(None, 48)
		score_text = font.render("Score: " + str(self.score), True,
								 (255,0,0))
		self.pantalla.blit(score_text, (0, 0))

		self.bola.mover(self.matriz)

		pygame.display.update()

if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
	juego = Juego()
	juego.jugar()