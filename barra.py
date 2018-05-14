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
    def __init__(self,x,y,ancho,largo):
        self.ancho = ancho
        self.largo = largo
        self.x = x
        self.y =y

    def posicionar_barra(self):
        self.ancho 
        self.largo

    def mover(self,vy,matriz):
        matriz[self.y][self.x] = 0
        self.y += vy
        matriz[self.y][self.x] = 1
