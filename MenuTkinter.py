from juego import *
from tkinter import *

window = Tk ( ) #hace la ventana
window.title ("PONG MENU") #le pone el título a la ventana
window.minsize (720, 480) #define el tamaño de la ventana
window.resizable (width = NO, height = NO) #el tamaño no se puede modificar
window.config(bg="#001939")

def Single_humano():
	if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
		juego = Juego("Single", 1, "humano")
		juego.jugar()

def Single_cpu():
	if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
		juego2 = Juego("Single", 1, "cpu")
		juego2.jugar()


def Double_humano():
	if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
		juego = Juego("Double", 1, "humano")
		juego.jugar()

def Double_cpu():
	if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
		juego2 = Juego("Double", 1, "cpu")
		juego2.jugar()


boton = Button (window, text = "Single_humano", font = ("arial", 12), width = 12, command = Single_humano)
boton.place (x = 100, y = 100)
boton2 = Button (window, text = "Single_cpu", font = ("arial", 12), width = 12, command = Single_cpu)
boton2.place (x = 250, y = 100)
boton4 = Button (window, text = "Double_humano", font = ("arial", 12), width = 12, command = Double_humano)
boton4.place (x = 100, y = 200)
boton5 = Button (window, text = "Double_cpu", font = ("arial", 12), width = 12, command = Double_cpu)
boton5.place (x = 250, y = 200)

mainloop()