class Barra_doble:
    def __init__(self,x,y,largo):
        self.ancho = 1
        self.largo = largo
        self.x = x
        self.y =y
        self.paleta_doble_posicion = [[],[]]
    def posicionar(self,matriz):
        for n in range(self.largo):
            self.paleta_doble_posicion[0].append((self.x-self.largo-1)+n)
        for n in range(self.largo):
            self.paleta_doble_posicion[1].append((self.x+1)+n)
        for posicion in self.paleta_doble_posicion[0]:
            matriz[posicion][self.y] = 1
        for posicion in self.paleta_doble_posicion[1]:
            matriz[posicion][self.y] = 1
    def mover(self,movimiento,matriz):
        n = len(self.paleta_doble_posicion[0])
        if movimiento == -1:
            if self.paleta_doble_posicion[0][0] > 0:
                matriz[self.paleta_doble_posicion[0][n-1]][self.y] = 0
                matriz[self.paleta_doble_posicion[1][n-1]][self.y] = 0
                for i in range(n):
                    self.paleta_doble_posicion[0][i] += movimiento
                    self.paleta_doble_posicion[1][i] += movimiento
                    matriz[self.paleta_doble_posicion[0][i]][self.y] = 1
                    matriz[self.paleta_doble_posicion[1][i]][self.y] = 1
        else:
            if self.paleta_doble_posicion[1][n-1] < 24:
                matriz[self.paleta_doble_posicion[0][0]][self.y] = 0
                matriz[self.paleta_doble_posicion[1][0]][self.y] = 0
                for i in range(n):
                    self.paleta_doble_posicion[0][i] += movimiento
                    self.paleta_doble_posicion[1][i] += movimiento
                    matriz[self.paleta_doble_posicion[0][i]][self.y] = 1
                    matriz[self.paleta_doble_posicion[1][i]][self.y] = 1

