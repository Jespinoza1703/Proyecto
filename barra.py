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
        	matriz[self.y+n][self.x] = 1

    def mover(self,vy,matriz):
        if vy == -1:
            matriz[self.y][self.x] = 0
            self.y -= vy
            matriz[self.y][self.x] = 1
        elif vy == 1 and self.y > 0:
            matriz[self.y + self.largo - 1][self.x] = 0
            self.y -= vy
            matriz[self.y][self.x] = 1

