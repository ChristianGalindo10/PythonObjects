from tkinter import *
from tkinter import ttk
from modelo.figuras.Cuadrilatero import Cuadrilatero
from modelo.figuras.Circulo import Circulo
from acciones.ControladorAcciones import ControladorAcciones

class PanelBotones:
    def __init__(self, ventana):
        control = ControladorAcciones(ventana)
        ttk.Button(ventana.ventana, text='Salir', command=ventana.ventana.destroy).pack(side=BOTTOM)
        ttk.Button(ventana.ventana, text='Circulo', command=control.circulo).pack(side=BOTTOM)
        ttk.Button(ventana.ventana, text='Cuadrilatero', command=control.cuadrilatero).pack(side=BOTTOM)
    