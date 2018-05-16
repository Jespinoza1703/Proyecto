from juego import *
from tkinter import *

window = Tk ( ) #hace la ventana
window.title ("PONG MENU") #le pone el título a la ventana
window.minsize (720, 480) #define el tamaño de la ventana
window.resizable (width = NO, height = NO) #el tamaño no se puede modificar
window.config(bg="#001939")

def nivel1():
	if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
		juego = Juego(Barra(1,2,9),Barra_doble(38,12,33,3,9),0.1)
		juego.jugar()

def nivel2():
	if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
		juego2 = Juego(Barra(1,2,9),Barra_doble(38,12,33,3,9),0.07)
		juego2.jugar()

def nivel3():
	if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
		juego3 = Juego(Barra(1,2,9),Barra_doble(38,12,33,3,9),0.04)
		juego3.jugar()


boton = Button (window, text = "Nivel1", font = ("arial", 12), width = 6, command = nivel1)
boton.place (x = 100, y = 100)
boton2 = Button (window, text = "Nivel2", font = ("arial", 12), width = 6, command = nivel2)
boton2.place (x = 200, y = 100)
boton3 = Button (window, text = "Nivel3", font = ("arial", 12), width = 6, command = nivel3)
boton3.place (x = 300, y = 100)


mainloop()