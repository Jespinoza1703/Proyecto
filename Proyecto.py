import pygame as pygame
import time as time
pygame.init()

ancho = 900
largo = 700

negro = (0, 0, 0)
blanco = (255, 255, 255)
azul = (0,0,255)
rojo = (255,0,0)
verde = (0,255,0)
rojo1 = (150, 0, 0)
verde1 = (0,150,0)
azul1 = (0,0,150)


gameDisplay = pygame.display.set_mode((ancho, largo)) #tamaño de la ventana
pygame.display.set_caption("Borrador") #titulo
clock = pygame.time.Clock()


class Figura():
	def __init__(self,x_fig,y_fig,ancho_fig,largo_fig,color_fig=blanco):#,color):

		self.__ancho_fig = ancho_fig
		self.__largo_fig = largo_fig
		self.__color_fig = color_fig

		self.image = pygame.Surface((self.__ancho_fig,self.__largo_fig))
		self.image.fill(self.__color_fig)
		self.rect = self.image.get_rect()
		self.rect.x = x_fig
		self.rect.y = y_fig


