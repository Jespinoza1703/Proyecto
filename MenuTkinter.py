from juego import *
from tkinter import *

window = Tk ( ) #hace la ventana
window.title ("PONG MENU") #le pone el título a la ventana
window.minsize (720, 480) #define el tamaño de la ventana
window.resizable (width = NO, height = NO) #el tamaño no se puede modificar
window.config(bg="#001939")

def nivel1():
	if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
		juego = Juego(Barra(1,2,9),Barra_doble(38,12,33,3,9),0.06)
		juego.jugar()

boton = Button (window, text = "Nivel1", font = ("arial", 12), width = 6, command = nivel1)
boton.place (x = 100, y = 100)

mainloop()