import tkinter as Label

class Rotulo(Label):
    def init (self, texto) -> None:
        super(). init (text=texto)

    def configura_grid(self, fileira: int, coluna: int) -> None:
        self.grid(row = fileira, column = coluna)