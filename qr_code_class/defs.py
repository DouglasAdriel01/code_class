import tkinter as tk

class Main(tk.Tk):
    def init (self) -> None:
        super().init()

    def configura_titulo(self, titulo:str) -> None:
        self.title(titulo)

    def configura_coordenadas(self, cooredenadax: int, coordenaday: int) -> None:
        self.config(padx= cooredenadax, pady= coordenaday)