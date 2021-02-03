import tkinter as tk

class Screen():
    def __init__(self):
        self.window = self.createWindow()

    def createWindow(self):
        window = tk.Tk()
        window.title("Jeu des allumettes")
        window.iconbitmap("icon.ico")
        window.geometry("1000x600")
        window.resizable(width=False, height=False)
        window.config(background="grey")

        return window