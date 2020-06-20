from tkinter import *
from tkinter import ttk
from modelo.figuras.Cuadrilatero import Cuadrilatero
from modelo.figuras.Circulo import Circulo

class ControladorAcciones:
    def __init__(self,ventana):
        self.circ = Circulo(150,180,3,"white",100) 
        self.c = Cuadrilatero(100,100,1,'red',25,30)
        self.ventana = ventana

    def circulo(self):
        self.circ.dibujar(self.ventana.canvas)
        
    def cuadrilatero(self):
        self.c.dibujar(self.ventana.canvas)