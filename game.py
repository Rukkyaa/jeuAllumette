from config import Config
import tkinter as tk
config = Config()
class Game():
    def __init__(self):
        self.numberOfAllumettes = int(config.number_allumettes)
