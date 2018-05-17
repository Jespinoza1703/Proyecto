from juego import *
from tkinter import *

window = Tk ( ) #hace la ventana
window.title ("Pong") #le pone el título a la ventana
window.minsize(800, 500) #define el tamaño de la ventana
window.resizable (width = NO, height = NO) #el tamaño no se puede modificar
window.config(bg="black")

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


#label de logo principal
mainlogo_label = Label(window, image = mainlogo)
mainlogo_label.place(x = 30, y = 45)

#botones de inicio de juego
oneplayer_button = Button(window, image = racket1cpuicon, command = Single_cpu)
oneplayer_button.place(x = 300, y = 100)
twoplayer_button = Button(window, image = racket12picon, command = Single_humano)
twoplayer_button.place(x = 300, y = 275)
oneplayer2r_button = Button(window, image = racket2cpuicon, command = Double_cpu)
oneplayer2r_button.place(x = 550, y = 100)
twoplayer2r_button = Button(window, image = racket22picon, command = Double_humano)
twoplayer2r_button.place(x = 550, y= 275)
about_button = Button(window, image = abouticon)
about_button.place(x = 50, y = 400)
help_button = Button(window, image = helpicon)
help_button.place(x = 50, y = 300)

mainloop()
