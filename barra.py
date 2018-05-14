# Clase Barra:
# Atributos:
# x
# y
# ancho
# largo
# vel_y
#######################
# Metodos:
# mover_barra()

class Barra:
    def __init__(self,x,y,largo):
        self.ancho = 1
        self.largo = largo
        self.x = x
        self.y =y

    def posicionar(self,matriz):
        for n in range(self.largo):
        	matriz[self.y+n][self.x]

    def mover(self,vy,matriz):
        matriz[self.y][self.x] = 0
        self.y += vy
        matriz[self.y][self.x] = 1
