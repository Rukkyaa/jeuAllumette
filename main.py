import tkinter as tk
from config import Config
from game import Game
from screen import Screen
from function import *
config = Config()
game = Game()
window = Screen().window

#Window creation:
main_frame = tk.Frame(window, bg = "grey", width = 1280, height = 720,  )
image = tk.PhotoImage(file = "allumettes.gif")

#FUNCTION
def lose():
    widgets = [title, canvas, allumettes]
    actualPlayer = player.cget("text")
    for i in widgets:
        i.grid_forget()

    loseText = tk.Label(main_frame, bg = "grey",fg = "red", text= "Le {} a perdu !".format(actualPlayer), font = ("Helvetica", 25))
    loseText.grid(row = 0, column = 0, pady = 200)

def nextPlayer():
    name = player.cget("text")

    if name == "Joueur 1":
        player.configure(text = "Joueur 2")
    else :
        player.configure(text="Joueur 1")

def button_1():
    canvas = tk.Canvas(main_frame, bg = "grey", width = 700, height = 100, bd = 0, highlightthickness=0)
    placement_allumette(canvas, image, game.numberOfAllumettes, 1)
    canvas.grid(row=1, column=0, pady=50)
    game.numberOfAllumettes -=1

    if game.numberOfAllumettes <= 0:
        lose()
    nextPlayer()

def button_2():
    canvas = tk.Canvas(main_frame, bg = "grey", width = 700, height = 100, bd = 0, highlightthickness=0)
    placement_allumette(canvas, image, game.numberOfAllumettes, 2)
    canvas.grid(row=1, column=0, pady=50)
    game.numberOfAllumettes -=2

    if game.numberOfAllumettes <= 0:
        lose()
    nextPlayer()
def button_3():
    canvas = tk.Canvas(main_frame, bg = "grey", width = 700, height = 100, bd = 0, highlightthickness=0)
    placement_allumette(canvas, image, game.numberOfAllumettes, 3)
    canvas.grid(row=1, column=0, pady=50)
    game.numberOfAllumettes -=3

    if game.numberOfAllumettes <= 0:
        lose()
    nextPlayer()
#title
title = tk.Label(main_frame, bg = "grey", text= "JEU DES ALLUMETTES", font = ("Helvetica", 25))
title.grid(row = 0, column = 0, pady = 50)

#canva
canvas = tk.Canvas(main_frame, bg = "grey", width = 700, height = 100, bd = 0, highlightthickness=0)
placement_allumette(canvas, image, game.numberOfAllumettes, 0)
canvas.grid(row = 1, column = 0, pady = 50)

#TestFrame
allumettes = tk.Frame(main_frame, bg = "grey", width = 1280, height = 200)
allumettes.grid(row = 2, column = 0, pady = 50)

#First button
one_button = tk.Button(allumettes, text = "1 allumette", bg = "grey", command = button_1)
one_button.pack(side = tk.LEFT)
#Second button
two_button = tk.Button(allumettes, text = "2 allumettes", bg = "grey", command = button_2)
two_button.pack(side = tk.LEFT, padx = 75)
#Third button
three_button = tk.Button(allumettes, text = "3 allumettes", bg = "grey", command = button_3)
three_button.pack(side = tk.LEFT)

#Player
player = tk.Label(main_frame, bg = "grey",fg = "red", text= "Joueur 1", font = ("Helvetica", 25))
player.grid(row = 3, column = 0, pady = 10)

#Barre menu
menu_barre =  tk.Menu(window)
file_menu = tk.Menu(menu_barre, tearoff = 0)
file_menu.add_command(label = "Quitter", command = window.quit)
menu_barre.add_cascade(label = "Option", menu = file_menu)
window.config(menu = menu_barre)

main_frame.pack()
window.mainloop()
