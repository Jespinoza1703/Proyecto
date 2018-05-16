from juego import *
from tkinter import *

window = Tk ( ) #hace la ventana
window.title ("PONG MENU") #le pone el título a la ventana
window.minsize (720, 480) #define el tamaño de la ventana
window.resizable (width = NO, height = NO) #el tamaño no se puede modificar
window.config(bg="#001939")

def Single_nivel1():
	if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
		juego = Juego("Single", 1)
		juego.jugar()

def Single_nivel2():
	if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
		juego2 = Juego("Single", 2)
		juego2.jugar()

def Single_nivel3():
	if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
		juego3 = Juego("Single", 3)
		juego3.jugar()

def Double_nivel1():
	if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
		juego = Juego("Double", 1)
		juego.jugar()

def Double_nivel2():
	if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
		juego2 = Juego("Double", 2)
		juego2.jugar()

def Double_nivel3():
	if __name__ == "__main__":#cuando le diga ejecutar, que llame primero al condicional Pong, es lo primero que se va a ejecutar
		juego3 = Juego("Double", 3)
		juego3.jugar()


boton = Button (window, text = "Single_Nivel1", font = ("arial", 12), width = 12, command = Single_nivel1)
boton.place (x = 100, y = 100)
boton2 = Button (window, text = "Single_Nivel2", font = ("arial", 12), width = 12, command = Single_nivel2)
boton2.place (x = 250, y = 100)
boton3 = Button (window, text = "Single_Nivel3", font = ("arial", 12), width = 12, command = Single_nivel3)
boton3.place (x = 400, y = 100)
boton4 = Button (window, text = "Double_Nivel1", font = ("arial", 12), width = 12, command = Double_nivel1)
boton4.place (x = 100, y = 200)
boton5 = Button (window, text = "Double_Nivel2", font = ("arial", 12), width = 12, command = Double_nivel2)
boton5.place (x = 250, y = 200)
boton6 = Button (window, text = "Double_Nivel3", font = ("arial", 12), width = 12, command = Double_nivel3)
boton6.place (x = 400, y = 200)


mainloop()