from juego import *
from tkinter import *

window = Tk ( ) #hace la ventana
window.title ("Pong") #le pone el título a la ventana
window.minsize(800, 500) #define el tamaño de la ventana
window.resizable (width = NO, height = NO) #el tamaño no se puede modificar
window.config(bg="white")

#funcion para cargar imagenes
def loadPicture(name):
        route = os.path.join('images', name)
        photo = PhotoImage(file = route)
        return photo

#carga de imagenes
racket1cpuicon = loadPicture('1racketcpu.gif')
racket12picon = loadPicture('1racket2p.gif')
racket2cpuicon = loadPicture('2racketcpu.gif')
racket22picon = loadPicture('2racket2p.gif')
mainlogo = loadPicture('mainlogo.gif')
racket2icon = loadPicture('2racket.gif')
abouticon = loadPicture('abouticon.gif')
cpuicon = loadPicture('cpuicon.gif')
helpicon = loadPicture('helpicon.gif')

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

#labels
mainlogo_label = Label(window, image = mainlogo)
mainlogo_label.place(x = 30, y = 45)
oneplayer_label = Label(window, text = '1 Racket AI', font = 'Helvetica 24')
oneplayer_label.place(x = 315, y = 195)
oneplayertworacket_label = Label(window, text = '2 Rackets AI', font = 'Helvetica 24')
oneplayertworacket_label.place(x = 585, y = 195)
twoplayer_label = Label(window, text = '1 Racket 2P', font = 'Helvetica 24')
twoplayer_label.place(x = 320, y = 370)
twoplayertworacket_label = Label(window, text = '2 Rackets 2P', font = 'Helvetica 24')
twoplayertworacket_label.place(x = 585, y = 370)
about_label = Label(window, text = 'About', font = 'Helvetica 24')
about_label.place(x = 130, y = 410)
help_label = Label(window, text = 'How to play', font = 'Helvetica 24')
help_label.place(x = 130, y = 310)


#botones de inicio de juego
oneplayer_button = Button(window, image = racket1cpuicon, command = Single_nivel1)
oneplayer_button.place(x = 300, y = 100)
twoplayer_button = Button(window, image = racket12picon)
twoplayer_button.place(x = 300, y = 275)
oneplayer2r_button = Button(window, image = racket2cpuicon)
oneplayer2r_button.place(x = 550, y = 100)
twoplayer2r_button = Button(window, image = racket22picon)
twoplayer2r_button.place(x = 550, y= 275)
about_button = Button(window, image = abouticon)
about_button.place(x = 50, y = 400)
help_button = Button(window, image = helpicon)
help_button.place(x = 50, y = 300)

boton2 = Button (window, text = "Single_Nivel2", font = ("arial", 12), width = 12, command = Single_nivel2)
boton2.place (x = 250, y = 400)
boton3 = Button (window, text = "Single_Nivel3", font = ("arial", 12), width = 12, command = Single_nivel3)
boton3.place (x = 400, y = 400)
boton4 = Button (window, text = "Double_Nivel1", font = ("arial", 12), width = 12, command = Double_nivel1)
boton4.place (x = 100, y = 450)
boton5 = Button (window, text = "Double_Nivel2", font = ("arial", 12), width = 12, command = Double_nivel2)
boton5.place (x = 250, y = 450)
boton6 = Button (window, text = "Double_Nivel3", font = ("arial", 12), width = 12, command = Double_nivel3)
boton6.place (x = 400, y = 450)


mainloop()
