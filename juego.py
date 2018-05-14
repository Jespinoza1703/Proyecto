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