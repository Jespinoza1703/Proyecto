# Pong v1.0
# II Tarea Programada
# Taller de Programación
# Estudiantes: Abigail Abarca. Jessica Espinoza. Alejandro Ibarra
# Profesor: Jeff Schmidt Peralta
# I Semestre 2018.

from juego import *
from tkinter import *
import os
import pygame

# Matriz con lista de textos en ingles y español
traduccion =[["1 Paleta IA", "1 Racket AI"], #0
               ["Cambiar el idioma", "Change language"],#1
               ["2 Paletas IA", "2 Rackets AI"],#2
               ["1 Paleta 2J", "1 Racket 2P"],#3
               ["2 Paletas 2J", "2 Rackets 2P"],#4
               ["¿Cómo jugar?", "How to play"],#5
               ["Acerca de", "About"],#6
                ]
 
# Variables globales
IDIOMA = 0
ESP = 0
ENG = 1
music = True

# Hace la ventana
ventana = Tk ( ) 
# Le pone el título a la ventana
ventana.title ("Pong") 
# Define el tamaño de la ventana
ventana.minsize(800, 500) 
# El tamaño no se puede modificar
ventana.resizable (width = NO, height = NO) 
ventana.config(bg="white")

# Iniciar Pygame
pygame.init()

# Funcion para cambiar idioma de textos
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

# Funcion para cargar imagenes
def loadPicture(name):
        route = os.path.join("images", name)
        photo = PhotoImage(file = route)
        return photo

# Funcion para reproducir la musica
def playMusic():
	pygame.mixer.Sound(os.path.join("sounds", "music.ogg")).play(loops = -1)

playMusic()

# Carga de imagenes
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
python = loadPicture("python.gif")

#Opcion de jugar con una paleta contra otro humano
def Single_humano():
	ventana.withdraw()
	juego = Juego("Single", 1, "humano")
	juego.jugar()

# Opcion de jugar con una paleta contra el CPU
def Single_cpu():
	ventana.withdraw()
	juego2 = Juego("Single", 1, "cpu")
	juego2.jugar()

# Opcion de jugar con dos paletas contra otro humano
def Double_humano():
	ventana.withdraw()
	juego = Juego("Double", 1, "humano")
	juego.jugar()

# Opcion de jugar con dos paletas contra el CPU
def Double_cpu():
	ventana.withdraw()
	juego2 = Juego("Double", 1, "cpu")
	juego2.jugar()

# Ventana de informacion de programadores
def about_ventana():
	ventana.withdraw()
	aboutventana = Toplevel()
	aboutventana.title("About")
	aboutventana.minsize(800, 500)
	aboutventana.resizable(width = NO, height = NO)

	aboutcanvas = Canvas(aboutventana, width = 800, height = 500, bg = "white")
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
	pythonpic = Button(aboutcanvas, image = python)
	pythonpic.place(x = 740, y = 10)

	# Para ir atras al menu
	def back():
		aboutventana.destroy()
		ventana.deiconify()

	backbutton = Button(aboutcanvas, image = backicon, command = back)
	backbutton.place(x = 20, y = 20)

# Ventana de instrucciones/ayuda
def help_ventana(): 
	ventana.withdraw()
	helpventana = Toplevel()
	helpventana.title("About")
	helpventana.minsize(800, 500)
	helpventana.resizable(width = NO, height = NO)

	helpcanvas = Canvas(helpventana, width = 800, height = 500)
	helpcanvas.place(x = 0, y = 0)

	instructionstitle = Label(helpventana, text = "Instructions/Instrucciones", font = "Helvetica 28")
	instructionstitle.place(x = 240, y = 40)

	# Instrucciones, texto
	instructions = Label(helpventana, text = "1. Select the game mode\n2. If you get more than 5 points, you level up.\n3. There are 3 levels, every level speeds the ball up and reduces the\nlength of the paddle.", justify = LEFT, font = "Helvetica 24")
	instructions.place(x = 50, y = 125)
	instructionsesp = Label(helpventana, text = "1. Selecciona el modo de juego.\n2. Si ganas más de 5 puntos, subes de nivel.\n3. Hay 3 niveles, cada nivel aumenta la velocidad de la bola y reduce\nla longitud de la paleta.", justify = LEFT, font = "Helvetica 24")
	instructionsesp.place(x = 50, y = 300)

	# Para ir atras en el menu
	def back(): 
		helpventana.destroy()
		ventana.deiconify()

	backbutton = Button(helpcanvas, image = backicon, command = back)
	backbutton.place(x = 20, y = 20)

# Textos e imagenes de menu
mainlogo_label = Label(ventana, image = mainlogo)
mainlogo_label.place(x = 30, y = 45)
oneplayer_label = Label(ventana, text=traduccion[0][IDIOMA], font = "Helvetica 20")
oneplayer_label.place(x = 315, y = 195)
oneplayertworacket_label = Label(ventana, text=traduccion[2][IDIOMA], font = "Helvetica 20")
oneplayertworacket_label.place(x = 585, y = 195)
twoplayer_label = Label(ventana, text=traduccion[3][IDIOMA], font = "Helvetica 20")
twoplayer_label.place(x = 320, y = 370)
twoplayertworacket_label = Label(ventana, text=traduccion[4][IDIOMA], font = "Helvetica 20")
twoplayertworacket_label.place(x = 585, y = 370)
about_label = Label(ventana, text=traduccion[6][IDIOMA], font = "Helvetica 20")
about_label.place(x = 110, y = 410)
help_label = Label(ventana, text=traduccion[5][IDIOMA], font = "Helvetica 20")
help_label.place(x = 110, y = 310)

# Botones de inicio de juego
oneplayer_button = Button(ventana, image = racket1cpuicon, command = Single_cpu)
oneplayer_button.place(x = 330, y = 100)
twoplayer_button = Button(ventana, image = racket12picon, command = Single_humano)
twoplayer_button.place(x = 330, y = 275)
oneplayer2r_button = Button(ventana, image = racket2cpuicon, command = Double_cpu)
oneplayer2r_button.place(x = 580, y = 100)
twoplayer2r_button = Button(ventana, image = racket22picon, command = Double_humano)
twoplayer2r_button.place(x = 580, y= 275)
about_button = Button(ventana, image = abouticon, command = about_ventana)
about_button.place(x = 50, y = 400)
help_button = Button(ventana, image = helpicon, command = help_ventana)
help_button.place(x = 50, y = 300)
cambiarIdioma = Button(ventana,text=traduccion[1][IDIOMA], font = "Helvetica 16", command = cambiarIdioma)
cambiarIdioma.place(x = 600, y = 40)

mainloop()
