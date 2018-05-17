#Pong v1.0
#II Tarea Programada
#Taller de Programación
#Estudiantes: Abigail Abarca. Jessica Espinoza. Alejandro Ibarra
#I Semestre 2018.

from juego import *
from tkinter import *

traduccion =[["1 Paleta IA", "1 Racket AI"], #0
               ["Cambiar el idioma", "Change language"],#1
               ["2 Paletas IA", "2 Rackets AI"],#2
               ["1 Paleta 2J", "1 Racket 2P"],#3
               ["2 Paletas 2J", "2 Rackets 2P"],#4
               ["¿Cómo jugar?", "How to play"],#5
               ["Acerca de", "About"],#6
                ]
 
IDIOMA = 0
ESP = 0
ENG = 1

window = Tk ( ) #hace la ventana
window.title ("Pong") #le pone el título a la ventana
window.minsize(800, 500) #define el tamaño de la ventana
window.resizable (width = NO, height = NO) #el tamaño no se puede modificar
window.config(bg="white")

def cambiarIdioma():
    global IDIOMA
    IDIOMA = 1 - IDIOMA
    cambiarIdioma.config(text=traduccion[1][IDIOMA])
    oneplayer_label.config(text=traduccion[0][IDIOMA])
    oneplayertworacket_label.config(text=traduccion[2][IDIOMA])
    twoplayer_label.config(text=traduccion[3][IDIOMA])
    twoplayertworacket_label.config(text=traduccion[4][IDIOMA])
    help_label.config(text=traduccion[5][IDIOMA])
    about_label.config(text=traduccion[6][IDIOMA])
#funcion para cargar imagenes
def loadPicture(name):
        route = os.path.join("images", name)
        photo = PhotoImage(file = route)
        return photo

#carga de imagenes
racket1cpuicon = loadPicture("1racketcpu.gif")
racket12picon = loadPicture("1racket2p.gif")
racket2cpuicon = loadPicture("2racketcpu.gif")
racket22picon = loadPicture("2racket2p.gif")
mainlogo = loadPicture("mainlogo.gif")
racket2icon = loadPicture("2racket.gif")
abouticon = loadPicture("abouticon.gif")
cpuicon = loadPicture("cpuicon.gif")
helpicon = loadPicture("helpicon.gif")
backicon = loadPicture("backicon.gif")
abigail = loadPicture("abigail.gif")
alejandro = loadPicture("alejandro.gif")
jessica = loadPicture("jessica.gif")

def Single_humano():
	window.withdraw()
	juego = Juego("Single", 1, "humano")
	juego.jugar()

def Single_cpu():
	window.withdraw()
	juego2 = Juego("Single", 1, "cpu")
	juego2.jugar()


def Double_humano():
	window.withdraw()
	juego = Juego("Double", 1, "humano")
	juego.jugar()

def Double_cpu():
	window.withdraw()
	juego2 = Juego("Double", 1, "cpu")
	juego2.jugar()


def about_window():
	window.withdraw()
	aboutwindow = Toplevel()
	aboutwindow.title("About")
	aboutwindow.minsize(800, 500)
	aboutwindow.resizable(width = NO, height = NO)

	aboutcanvas = Canvas(aboutwindow, width = 800, height = 500, bg = "white")
	aboutcanvas.place(x = 0, y = 0)

	aboutlabel = Label(aboutcanvas, text = "About the programmers", font = "Helvetica 30")
	aboutlabel.place(x = 240, y = 30)
	abigailpic = Label(aboutcanvas, image = abigail)
	abigailpic.place(x = 50, y = 120)
	abigailinfo = Label(aboutcanvas, text = "Abigail Abarca", font = "Helvetica 20")
	abigailinfo.place(x = 50, y = 350)
	alejandropic = Label(aboutcanvas, image = alejandro)
	alejandropic.place(x = 550, y = 130)
	alejandroinfo = Label(aboutcanvas, text = "Alejandro Ibarra", font = "Helvetica 20")
	alejandroinfo.place(x = 550, y = 350)
	jessicapic = Label(aboutcanvas, image = jessica)
	jessicapic.place(x = 280, y = 130)
	jessicainfo = Label(aboutcanvas, text = "Jessica Espinoza", font = "Helvetica 20")
	jessicainfo.place(x = 275, y = 350)

	def back():
		aboutwindow.destroy()
		window.deiconify()

	backbutton = Button(aboutcanvas, image = backicon, command = back)
	backbutton.place(x = 20, y = 20)

def help_window(): #ventana de instrucciones/ayuda
	window.withdraw()
	helpwindow = Toplevel()
	helpwindow.title("About")
	helpwindow.minsize(800, 500)
	helpwindow.resizable(width = NO, height = NO)

	helpcanvas = Canvas(helpwindow, width = 800, height = 500)
	helpcanvas.place(x = 0, y = 0)

	instructionstitle = Label(helpwindow, text = "Instructions/Instrucciones", font = "Helvetica 28")
	instructionstitle.place(x = 240, y = 40)

	#instrucciones, texto
	instructions = Label(helpwindow, text = "1. Select the game mode\n2. If you get more than 5 points, you level up.\n3. There are 3 levels, every level speeds the ball up and reduces the\nlength of the paddle.", justify = LEFT, font = "Helvetica 24")
	instructions.place(x = 50, y = 125)
	instructionsesp = Label(helpwindow, text = "1. Selecciona el modo de juego.\n2. Si ganas más de 5 puntos, subes de nivel.\n3. Hay 3 niveles, cada nivel aumenta la velocidad de la bola y reduce\nla longitud de la paleta.", justify = LEFT, font = "Helvetica 24")
	instructionsesp.place(x = 50, y = 300)

	def back(): #para ir atras en el menu
		helpwindow.destroy()
		window.deiconify()

	backbutton = Button(helpcanvas, image = backicon, command = back)
	backbutton.place(x = 20, y = 20)

mainlogo_label = Label(window, image = mainlogo)
mainlogo_label.place(x = 30, y = 45)
oneplayer_label = Label(window, text=traduccion[0][IDIOMA], font = "Helvetica 20")
oneplayer_label.place(x = 315, y = 195)
oneplayertworacket_label = Label(window, text=traduccion[2][IDIOMA], font = "Helvetica 20")
oneplayertworacket_label.place(x = 585, y = 195)
twoplayer_label = Label(window, text=traduccion[3][IDIOMA], font = "Helvetica 20")
twoplayer_label.place(x = 320, y = 370)
twoplayertworacket_label = Label(window, text=traduccion[4][IDIOMA], font = "Helvetica 20")
twoplayertworacket_label.place(x = 585, y = 370)
about_label = Label(window, text=traduccion[6][IDIOMA], font = "Helvetica 20")
about_label.place(x = 110, y = 410)
help_label = Label(window, text=traduccion[5][IDIOMA], font = "Helvetica 20")
help_label.place(x = 110, y = 310)



#botones de inicio de juego
oneplayer_button = Button(window, image = racket1cpuicon, command = Single_cpu)
oneplayer_button.place(x = 330, y = 100)
twoplayer_button = Button(window, image = racket12picon, command = Single_humano)
twoplayer_button.place(x = 330, y = 275)
oneplayer2r_button = Button(window, image = racket2cpuicon, command = Double_cpu)
oneplayer2r_button.place(x = 580, y = 100)
twoplayer2r_button = Button(window, image = racket22picon, command = Double_humano)
twoplayer2r_button.place(x = 580, y= 275)
about_button = Button(window, image = abouticon, command = about_window)
about_button.place(x = 50, y = 400)
help_button = Button(window, image = helpicon, command = help_window)
help_button.place(x = 50, y = 300)
cambiarIdioma = Button(window,text=traduccion[1][IDIOMA], font = "Helvetica 16", command = cambiarIdioma)
cambiarIdioma.place(x = 600, y = 40)

mainloop()
